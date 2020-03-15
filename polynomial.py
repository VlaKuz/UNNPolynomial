class Polynomial:
    def __init__(self, other):
        if isinstance(other, (list, tuple)):
            if len(other) == 0:
                raise AttributeError('Input data is empty')
            elif any(isinstance(coef, bool) for coef in other) or not all(isinstance(coef, int) for coef in other):
                raise TypeError('Incorrected value type of coefficients. Expected: int')
            elif all(coef == 0 for coef in other):
                other = [0]
            elif other[0] == 0:
                if isinstance(other, tuple):
                    other = list(other)
                while other[0] == 0:
                    other.remove(0)
        if isinstance(other, list):
            self.coeffs = other
        elif isinstance(other, tuple):
            self.coeffs = list(other)
        elif isinstance(other, Polynomial):
            self.coeffs = other.coeffs.copy()
        else:
            raise TypeError('Incorrected input data. Expected: list, tuple, Polynomial. Actual:' + str(type(other)))

    def __add__(self, other):
        result_sum = []
        if isinstance(other, int):
            result_sum = self.coeffs
            result_sum[-1] = self.coeffs[-1] + other
            return (Polynomial(result_sum))
        elif isinstance(other, Polynomial):
            if len(self.coeffs) > len(other.coeffs):

                while len(self.coeffs) > len(other.coeffs):
                    other.coeffs.insert(0,0)
            else:
                while len(self.coeffs) < len(other.coeffs):
                    self.coeffs.insert(0,0)
            for monom in range(len(self.coeffs)):
                result_sum.append(self.coeffs[monom] + other.coeffs[monom])
            while result_sum[0] == 0:
                result_sum.remove(0)
                if len(result_sum) > 0:
                    continue
                else:
                    return Polynomial([0])
            return Polynomial(result_sum)
        else:
            raise TypeError('Incorrected input data. Expected: int, Polynomial. Actual:' + str(type(other)))

    def __radd__(self, other):
        return(self.__add__(other))

    def __sub__(self, other):
        result_sum = []
        if isinstance(other, int):
            result_sum = self.coeffs
            result_sum[-1] = self.coeffs[-1] - other
            return (Polynomial(result_sum))
        elif isinstance(other, Polynomial):
            if len(self.coeffs) > len(other.coeffs):

                while len(self.coeffs) > len(other.coeffs):
                    other.coeffs.insert(0, 0)
            else:
                while len(self.coeffs) < len(other.coeffs):
                    self.coeffs.insert(0, 0)
            for monom in range(len(self.coeffs)):
                result_sum.append(self.coeffs[monom] - other.coeffs[monom])
            while result_sum[0] == 0:
                result_sum.remove(0)
                if len(result_sum) > 0:
                    continue
                else:
                    return Polynomial([0])
            return Polynomial(result_sum)
        else:
            raise TypeError('Incorrected input data. Expected: int, Polynomial. Actual:' + str(type(other)))

    def __rsub__(self, other):
        result_sum = []
        if not type(other) == Polynomial:
            result_sum =[-1 * tmp for tmp in self.coeffs]
            result_sum[-1] = other - self.coeffs[-1]
            return (Polynomial(result_sum))

    def __neg__(self):
        self.coeffs = [-coef for coef in self.coeffs]
        return self

    def __mul__(self, other):
        res_mult = []
        if isinstance(other, int):
            res_mult = [coeff * other for coeff in self.coeffs]
            return Polynomial(res_mult)
        elif isinstance(other, Polynomial):
            res_mult = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
            for step_self, coef_self in enumerate(self.coeffs):
                for step_other, coef_other in enumerate(other.coeffs):
                    res_mult[step_self + step_other] += coef_self * coef_other
            return Polynomial(res_mult)
        else:
            raise TypeError('Incorrected input data. Expected: int, Polynomial. Actual:' + str(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        else:
            raise TypeError('Incorrected input data. Expected: Polynomial. Actual:' + str(type(other)))
    def __ne__(self, other):
        if isinstance(other, Polynomial):
            return not (self.coeffs == other.coeffs)
        else:
            raise TypeError('Incorrected input data. Expected: Polynomial. Actual:' + str(type(other)))

    def __str__(self):
        string_polinom = []
        res_str = ''
        for step, coef_value in enumerate(reversed(self.coeffs)):
            if not coef_value == 0:
                if (step == 0):
                    x_name = str(coef_value)
                elif (step == 1):
                    if coef_value != 1 and coef_value != -1:
                        x_name = str(coef_value) + 'x'
                    elif coef_value == 1:
                        x_name = 'x'
                    else:
                        x_name = '-x'
                else:
                    if coef_value != 1 and coef_value != -1:
                        x_name = str(coef_value) + 'x^' + str(step)
                    elif coef_value == 1:
                        x_name = 'x^' + str(step)
                    else:
                        x_name = '-x^' + str(step)
                string_polinom.append(x_name)
        string_polinom.reverse()
        if string_polinom:
            res_str = ' + '.join(string_polinom)
            res_str = res_str.replace('+ -', '- ')
            return res_str
        else:
            return '0'

    def __repr__(self):
        return "Polynomial(" + str(self.coeffs) + ")"
