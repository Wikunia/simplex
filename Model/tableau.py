import numpy as np
import copy

class Tableau(object):
    def __init__(self, data=False, nof_var_cols=0, dual=False, obj_type=1, type=1,
                 row_to_var= False, variables= False, constraints=False,
                 obj_coefficients=False):
        self.MINIMIZE = -1
        self.MAXIMIZE = 1

        if data is False:
            data = np.zeros((1, 1))
        self._data = data
        self._nof_var_cols = nof_var_cols
        self._dual = dual
        self._obj_type = obj_type
        self._type = type
        if row_to_var is False:
            row_to_var = np.array([])
        self._row_to_var = row_to_var
        self._variables = variables
        self._constraints = constraints
        if obj_coefficients is False:
            obj_coefficients = np.array([])
        self._obj_coefficients = obj_coefficients

    def set_tableau(self, val):
        self._data = val

    def get_tableau(self):
        return self._data

    def get_obj(self):
        return self._data[-1]

    def set_obj(self, value):
        self._data[-1] = value

    def get_nof_var_cols(self):
        return self._nof_var_cols

    def set_nof_var_cols(self, value):
        self._nof_var_cols = value

    def get_bs(self):
        return self._data[:-1,-1]

    def set_bs(self, value):
        self._data[:-1,-1] = value

    def get_matrix(self):
        return self._data[:-1]

    def set_matrix(self, value):
        self._data[:-1] = value

    def get_A_star(self):
        return self._data[:-1, :self._nof_var_cols]

    def set_A_star(self, value):
        self._data[:-1, :self._nof_var_cols] = value

    def get_S_star(self):
        return self._data[:-1, self._nof_var_cols:-1]

    def set_S_star(self, value):
        self._data[:-1, self._nof_var_cols:-1] = value

    def get_y_star(self):
        return self._data[-1, self._nof_var_cols:-1]

    def set_y_star(self, value):
        self._data[-1, self._nof_var_cols:-1] = value

    def get_c_star(self):
        return self._data[-1, :self._nof_var_cols]

    def set_c_star(self, value):
        self._data[-1, :self._nof_var_cols] = value

    def get_dual(self):
        return self._dual

    def set_dual(self, value):
        self._dual = value

    def get_obj_type(self):
        return self._obj_type

    def set_obj_type(self, value):
        self._obj_type = value

    def get_type(self):
        return self._type

    def set_type(self, value):
        self._type = value

    def get_row_to_var(self):
        return self._row_to_var

    def set_row_to_var(self, value):
        self._row_to_var = value

    def get_variables(self):
        return self._variables

    def set_variables(self, value):
        self._variables = value

    def get_constraints(self):
        return self._constraints

    def set_constraints(self, value):
        self._constraints = value

    def get_obj_coefficients(self):
        return self._obj_coefficients

    def set_obj_coefficients(self, value):
        self._obj_coefficients = value


class TableauView(object):
    def __init__(self,tab_data=False):
        if tab_data is False:
            self.tab = Tableau()
        else:
            self.tab = tab_data

    def deepcopy(self):
        tableau = np.copy(self.tab.get_tableau())
        nof_var_cols = self.tab.get_nof_var_cols()
        dual = self.tab.get_dual()
        type = self.tab.get_type()
        obj_type = self.tab.get_obj_type()
        row_to_var = np.copy(self.tab.get_row_to_var())
        variables = copy.deepcopy(self.tab.get_variables())
        constraints = copy.deepcopy(self.tab.get_constraints())
        obj_coefficients = copy.deepcopy(self.tab.get_obj_coefficients())
        tab = Tableau(tableau, nof_var_cols, dual, obj_type, type, row_to_var,
                      variables, constraints, obj_coefficients)
        return TableauView(tab)

    @property
    def tableau(self):
        return self.tab.get_tableau()

    @tableau.setter
    def tableau(self, data):
        self.tab.set_tableau(data)

    @property
    def matrix(self):
        return self.tab.get_matrix()

    @matrix.setter
    def matrix(self, data):
        self.tab.set_matrix(data)

    @property
    def nof_var_cols(self):
        return self.tab.get_nof_var_cols()

    @nof_var_cols.setter
    def nof_var_cols(self, data):
        self.tab.set_nof_var_cols(data)

    @property
    def A_star(self):
        return self.tab.get_A_star()

    @A_star.setter
    def A_star(self, data):
        self.tab.set_A_star(data)

    @property
    def bs(self):
        return self.tab.get_bs()

    @bs.setter
    def bs(self, data):
        self.tab.set_bs(data)

    @property
    def obj(self):
        return self.tab.get_obj()

    @obj.setter
    def obj(self, data):
        self.tab.set_obj(data)

    @property
    def S_star(self):
        return self.tab.get_S_star()

    @S_star.setter
    def S_star(self, data):
        self.tab.set_S_star(data)

    @property
    def y_star(self):
        return self.tab.get_y_star()

    @y_star.setter
    def y_star(self, data):
        self.tab.set_y_star(data)

    @property
    def c_star(self):
        return self.tab.get_c_star()

    @c_star.setter
    def c_star(self, data):
        self.tab.set_c_star(data)

    @property
    def dual(self):
        return self.tab.get_dual()

    @dual.setter
    def dual(self, data):
        self.tab.set_dual(data)

    @property
    def type(self):
        return self.tab.get_type()

    @type.setter
    def type(self, data):
        self.tab.set_type(data)

    @property
    def row_to_var(self):
        return self.tab.get_row_to_var()

    @row_to_var.setter
    def row_to_var(self, data):
        self.tab.set_row_to_var(data)

    @property
    def variables(self):
        return self.tab.get_variables()

    @variables.setter
    def variables(self, data):
        self.tab.set_variables(data)

    @property
    def constraints(self):
        return self.tab.get_constraints()

    @constraints.setter
    def constraints(self, data):
        self.tab.set_constraints(data)

    @property
    def obj_coefficients(self):
        return self.tab.get_obj_coefficients()

    @obj_coefficients.setter
    def obj_coefficients(self, data):
        self.tab.set_obj_coefficients(data)

    @property
    def obj_type(self):
        return self.tab.get_obj_type()

    @obj_type.setter
    def obj_type(self, data):
        self.tab.set_obj_type(data)








