#Finance functions challenge
# present_value = float(input("please introduce present value: "))
# rate_of_return= float(input("please introduce the return rate % "))
# number_of_periods = float(input("please introduce the number of periods: "))
# future_value = present_value*(1+rate_of_return/100)**number_of_periods
# print (f"future value ${future_value:.2f}")

def future_value(present_value,rate_of_return,number_of_periods):
    return round(present_value*(1+rate_of_return/100)**number_of_periods,2)

#  Output in shell

# danielrosas@iMac-de-Daniel ThirdWeekCode % python3
# Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23)
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from Finance_functions import future_value
# >>> future_value(1000,0.1,5)
# 1005.0100100050004
# >>> future_value(1000,0.1,10)
# 1010.0451202102512
# >>>
