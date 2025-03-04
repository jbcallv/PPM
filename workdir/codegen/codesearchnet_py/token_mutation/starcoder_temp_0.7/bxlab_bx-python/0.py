def lF_value (ER,EF,dfnum,dfden):
    """
Returns an F-statistic given the following:
        ER  = error associated with the null null (the Restricted model)
        EF  = error associated with the hypothesis hypothesis (the full model)
        dfR-dfF = degrees of freedom of the numerator
        dfF = degrees of freedom associated with the denominator/Full model

Usage:   lF_value(ER,EF,dfnum,dfden)
"""
    F = (ER-EF)/(dfnum/dfden)
    return F

