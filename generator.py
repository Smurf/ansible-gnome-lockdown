import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
import os
import argparse

def gsettings_to_ansible_type(gsettings_type):
    """Maps GSettings type to Ansible type."""
    if gsettings_type == 'b':
        return 'bool'
    elif gsettings_type == 'i':
        return 'int'
    elif gsettings_type == 's':
        return 'str'
    else:
        # Default to string for unknown types
        return 'str'

def parse_schema(xml_file):
    """Parses a GSettings XML schema and extracts relevant information."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    schema_node = root.find('schema')
    if schema_node is None:
        raise ValueError("No schema found in XML file")

    schema_id = schema_node.get('id')
    schema_path = schema_node.get('path')

    keys = []
    for key_node in schema_node.findall('key'):
        key_name = key_node.get('name')
        key_type = key_node.get('type')

        default_node = key_node.find('default')
        # Defaults for strings are in quotes, so strip them
        key_default = default_node.text.strip("'") if default_node is not None else ''

        # Convert boolean defaults to Python booleans for Jinja2
        if key_type == 'b':
            key_default = key_default.lower() in ['true']

        summary_node = key_node.find('summary')
        key_summary = summary_node.text if summary_node is not None else ''

        description_node = key_node.find('description')
        key_description = description_node.text if description_node is not None else ''

        keys.append({
            'name': key_name,
            'ansible_type': gsettings_to_ansible_type(key_type),
            'default': key_default,
            'summary': key_summary,
            'description': key_description
        })

    return schema_id, schema_path, keys

def generate_module(schema_file, template_file, output_dir):
    """Generates an Ansible module from a schema and a Jinja2 template."""
    schema_id, schema_path, keys = parse_schema(schema_file)

    # Module name from schema id
    module_name = "gsettings_" + schema_id.replace('.', '_')

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(os.path.basename(template_file))

    # Render the template
    module_content = template.render(
        module_name=module_name,
        schema_id=schema_id,
        schema_path=schema_path,
        keys=keys
    )

    # Write the output file
    output_path = os.path.join(output_dir, module_name + ".py")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(module_content)

    print(f"Successfully generated module: {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate an Ansible module from a GSettings schema.")
    parser.add_argument("--schema", default="org.gnome.desktop.lockdown.gschema.xml", help="Path to the GSettings XML schema file.")
    parser.add_argument("--template", default="base_module_template.j2", help="Path to the Jinja2 template file.")
    parser.add_argument("--output-dir", default="generated_modules", help="Directory to save the generated module.")

    args = parser.parse_args()

    generate_module(args.schema, args.template, args.output_dir)
