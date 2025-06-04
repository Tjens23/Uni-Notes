```python
from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment

        variable = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(variable, assignment):
            if self.is_consistent(variable, value, assignment):
                assignment[variable] = value
                result = self.recursive_backtracking(assignment)
                if result is not None:
                    return result
                del assignment[variable]

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True

def create_South_America_csp():
    cr, p, col, ec, pe, ve, gu, su, gu_fr, br, bol, chi, par, uru, ar = 'Costa Rica' , 'Panama', 'Colombia', 'Ecuador', 'Peru', 'Venezuela', 'Guyana', 'Suriname', 'Guyana Fr', 'Brasil', 'Bolivia', 'Chile', 'Paraguay', 'Uruguay', 'Argentina'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cr, p, col, ec, pe, ve, gu, su, gu_fr, br, bol, chi, par, uru, ar]
    domains = {
        cr: values[:],
        p: values[:],
        col: values[:],
        ec: values[:],
        pe: values[:],
        ve: values[:],
        gu: values[:],
        su: values[:],
        gu_fr: values[:],
        br: values[:],
        bol: values[:],
        chi: values[:],
        par: values[:],
        uru: values[:],
        ar: values[:]
    }

    neighbors = {
        cr: [p],
        p: [cr, col],
        col: [p, ve, ec, pe, br],
        ec: [col,pe],
        pe: [ec,col,bol,br,chi],
        ve: [col, br, gu],
        gu: [ve, su, br],
        su: [gu, gu_fr, br],
        gu_fr: [su, br],
        br: [gu_fr, su, gu, ve, col, pe, bol, par, ar, uru],
        bol: [pe, br, par, ar, chi],
        chi: [pe, bol, ar],
        par: [bol, br, ar],
        uru: [br, ar],
        ar: [uru, br, par, bol, chi]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cr: constraint_function,
        p: constraint_function,
        col: constraint_function,
        ec: constraint_function,
        pe: constraint_function,
        ve: constraint_function,
        gu: constraint_function,
        su: constraint_function,
        gu_fr: constraint_function,
        br: constraint_function,
        bol: constraint_function,
        chi: constraint_function,
        par: constraint_function,
        uru: constraint_function,
        ar: constraint_function,
    }

    return CSP(variables, domains, neighbors, constraints)

def create_australia_csp():
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    #australia = create_australia_csp()
    #result = australia.backtracking_search()

    south_usa = create_australia_csp()
    result = south_usa.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
```