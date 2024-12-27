from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Module content data structure
module_content = {
'logic': {
        'name': 'Logic and Computation',
        'weeks': {
            'week1': {
                'title': 'Sets: The Language of Mathematics',
                'content': 'Content for Sets and Mathematics...'
            },
            'week2': {
                'title': 'Introduction to Logic: Propositional Logic',
                'content': 'Content for Propositional Logic...'
            },
            'week3': {
                'title': 'Valid Arguments and Logical Equivalences',
                'content': 'Content for Valid Arguments...'
            },
            'week4': {
                'title': 'Predicate Logic',
                'content': 'Content for Predicate Logic...'
            },
            'week5': {
                'title': 'Universal Conditional Statements and Logic Circuits',
                'content': 'Content for Logic Circuits...'
            },
            'week7': {
                'title': 'The Theory of Computation and Regular Expressions',
                'content': 'Content for Theory of Computation...'
            },
            'week8': {
                'title': 'Models of Computation: Finite State Automata',
                'content': 'Content for Finite State Automata...'
            },
            'week9': {
                'title': 'Context-Free Languages & Grammars',
                'content': 'Content for Context-Free Languages...'
            },
            'week10': {
                'title': 'Turing Machine and the Limits of Computability',
                'content': 'Content for Turing Machines...'
            },
            'week11': {
                'title': 'Combinatorics',
                'content': 'Content for Combinatorics...'
            }
        }
    },
    'programming': {
        'name': 'Introductory Programming',
        'weeks': {
            'week1': {
                'title': 'Introduction to Java',
                'content': 'Content for Java Introduction...'
            },
            'week2': {
                'title': 'Variables and Data Types',
                'content': 'Content for Variables and Data Types...'
            },
            'week3': {
                'title': 'Control Structures',
                'content': 'Content for Control Structures...'
            }
        }
    },
    'systems': {
        'name': 'Information Systems and Organisations',
        'weeks': {
            'block1': {
                'title': 'Information Systems',
                'content': 'Content for Information Systems...'
            },
            'block2': {
                'title': 'System Analysis & Design',
                'content': 'Content for System Analysis & Design...'
            },
            'block3': {
                'title': 'System Development Methodologies',
                'content': 'Content for System Development Methodologies...'
            }
        }
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/module/<module_name>')
def module(module_name):
    if module_name in module_content:
        return render_template('module.html', 
                             module=module_content[module_name],
                             module_name=module_name)
    return "Module not found", 404

if __name__ == '__main__':
    app.run(debug=True)