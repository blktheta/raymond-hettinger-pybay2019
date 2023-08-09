"""Fishinge
Strategy:   Repeat tasks manually until patterns emerge, then move to
            a function. Continue to generalize as needed.

Example:    Convert CSV to XML

Problem:    Convert a CSV file to XML

Programmers that begin with typing a function makes it harder to figure
out what is happening with print statements while debuging. The only
way to resolve this is by using breakpoints and pm (post mortem).

The example below shows the procedure of generalizing and emerging
pattern. Remove the ''' comment demarcation, and run the file.
After a step has been understood encapsulate the code again with '''.
"""
from xml.etree.ElementTree import Element, ElementTree, dump
import csv


"""
The code below doesn't feature any functions. Functions should be
avoided until natural patterns emerge within the code. The example
below features manually hardwired solutions. At this point
there is enogh information to establish patterns.
"""

root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = Element('person')
        person.text = '\n'      # debug
        person.tail = '\n'      # debug
        root.append(person)

        fn = Element('full_name')
        fn.text = f'{fname} {lname}'
        fn.tail = '\n'          # debug
        person.append(fn)

        jt = Element('job_title')
        jt.text = title
        jt.tail = '\n'
        person.append(jt)

dump(root)


'''
"""
Generlise the pattern by first cut & paste the emergin patterns into a
function. Intersting to note is that the moved code is note modified
within the function. This is considered minimal transformation.
"""

def add_fn():
    fn = Element('full_name')
    fn.text = f'{fname} {lname}'
    fn.tail = '\n'          # debug
    person.append(fn)

root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = Element('person')
        person.text = '\n'      # debug
        person.tail = '\n'      # debug
        root.append(person)

        add_fn()

        jt = Element('job_title')
        jt.text = title
        jt.tail = '\n'
        person.append(jt)

dump(root)
'''


'''
"""
Compare the differences between the patterns for creating 'full_name'
and 'job_title'. Find the difference by identifing related constant
values. A constant value that changes is called a variable. Pass in the
changing constant variable in the function.

This process is very methodological and slow working. When something
goes wrong it can be fixed by simple ctrl+z/version controlling. This
also saves a lot of debugging effort.
"""
def add_fn(tag, text):
    fn = Element(tag)
    fn.text = text
    fn.tail = '\n'          # debug
    person.append(fn)

root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = Element('person')
        person.text = '\n'      # debug
        person.tail = '\n'      # debug
        root.append(person)

        add_fn('full_name', f'{fname} {lname}')

        jt = Element('job_title')
        jt.text = title
        jt.tail = '\n'
        person.append(jt)

dump(root)
'''


'''
"""
To fully generalize the function comment out the patterns and insert
them through the established function. If it works make sure to
generalize the function and variable reference names in order to fit
with the pattern.
"""
def add_element(tag, text):
    elem = Element(tag)
    elem.text = text
    elem.tail = '\n'          # debug
    person.append(elem)

root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = Element('person')
        person.text = '\n'      # debug
        person.tail = '\n'      # debug
        root.append(person)

        add_element('full_name', f'{fname} {lname}')
        add_element('job_title', title)

        #jt = Element('job_title')
        #jt.text = title
        #jt.tail = '\n'
        #person.append(jt)

dump(root)
'''


'''
"""
With the generalized function established, adding new elements to the
xml tree should require less efforts. The important take on this
approach is that the generalized function was discovred and not
planned beforehand or written in advance.
"""
def add_element(tag, text):
    elem = Element(tag)
    elem.text = text
    elem.tail = '\n'          # debug
    person.append(elem)

root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = Element('person')
        person.text = '\n'      # debug
        person.tail = '\n'      # debug
        root.append(person)

        add_element('full_name', f'{fname} {lname}')
        add_element('job_title', title)
        add_element('work_phone', phone)
        add_element('work_email', email)

dump(root)
'''

'''
"""
Excercise:  Generalize the below, add_element(), function further to
            include a parental relationship. Making it general
            enough to create a person element with it.

Hint: Make sure to return the element

Solution is featured at the end of the file.
"""
def add_element(tag, text):
    elem = Element(tag)
    elem.text = text
    elem.tail = '\n'          # debug
    person.append(elem)


root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):

        # Code to generalize
        person = Element('person')
        person.text = '\n'      # debug
        person.tail = '\n'      # debug
        root.append(person)
        # -----

        add_element('full_name', f'{fname} {lname}')
        add_element('job_title', title)
        add_element('work_phone', phone)
        add_element('work_email', email)

dump(root)
'''

















"""
# Solution Example
def add_element(parent, tag, text='\n'):
    elem = Element(tag)
    elem.text = text
    elem.tail = '\n'          # debug
    parent.append(elem)
    return elem

root = Element('contact_list', status='Public', company='Raisins R Us, Inc')
root.text = '\n'    # debug
root.tail = '\n'    # debug

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = add_element(root, 'parent')
        add_element(person, 'full_name', f'{fname} {lname}')
        add_element(person, 'job_title', title)
        add_element(person, 'work_phone', phone)
        add_element(person, 'work_email', email)

dump(root)
"""


"""
# Bonus tip: Generalize further to include root element
def add_element(parent, tag, text='\n', **kwargs):
    elem = Element(tag, **kwargs)
    elem.text = text
    elem.tail = '\n'          # debug
    if parent is not None:
        parent.append(elem)
    return elem

root = add_element(None, 'contact_list', status='Public', company='Raisins R Us, Inc')

with open('raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        person = add_element(root, 'parent')
        add_element(person, 'full_name', f'{fname} {lname}')
        add_element(person, 'job_title', title)
        add_element(person, 'work_phone', phone)
        add_element(person, 'work_email', email)

dump(root)
"""
