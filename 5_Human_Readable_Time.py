
seconds = 86399


from math import floor

def make_readable(seconds):
    min = 60; hour = 3600
    hr = floor(seconds / hour); seconds = seconds - (hr * hour)
    mn = floor(seconds / min); seconds = seconds - (mn * min)
    return ('0' + str(hr))[-2:] + ':' + ('0' + str(mn))[-2:] + ":" + ('0' + str(seconds))[-2:]






Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")