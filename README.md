Template development exercise

Still extremely simple.

The idea was first to have a template hard coded in python structures and files with data, that would feed the template, in YAML format.

From this came the ridiculous idea of the name Yet Another Template Markup Language. So original that I beg you not to tell anybody.

At the end, obviously, both, template as data values, can be in both formats, python and YAML.

There are two classes:
    • OTempl, that receive template and values in structured data
    • OYatml, that receive the names of two YAML files, that feed the two needed structured data, template and values

The "O" at the beginning is from Oxigenai, my small programming company.

There is no error handling and the features are few.

The template data is a dictionary of "parts". The first part to be processed is the "base"
part.

Each part has blocks of template that can be:
    • pure text template
    • text with template variables (in string.Template style)
        ◦ the name of the parts is a name space for this variables
    • a list (or tuple) of other parts
    • a special block (with advanced functionalities)

Special block are dictionaries with "type", "name" and more values.
    • "name" is a name space for the variables inside the special block
    • "type" indicate the functionality of that block

There are only one special block functionality implemented:
    • "loop": that repeat something for the number of available values for the inside variables
    • inside actual loop special block there are a variable called "repeat", that has a template chunk to repeat

The values data is a dictionary of values obey the name spaces (part name, spatial "name" value) and has the name used in template.

The type of the values can be any, but can be special rules for special blocks, like: the variables in a name space of a loop are lists with the same size.
