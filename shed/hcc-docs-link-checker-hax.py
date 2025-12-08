import requests

good_url = 'https://access.redhat.com/documentation/en-us/red_hat_insights/1-latest/html/generating_advisor_service_reports/index'
bad_url = 'https://docs.redhat.com/en/documentation/red_hat_insights/1-latest/html/converting_from_a_linux_distribution_to_rhel_using_the_convert2rhel_utility_in_red_hat_insights/preparation-for-a-rhel-conversion-using-insights_converting-from-a-linux-distribution-to-rhel-in-insights'
print("This one should succeed\n========================\n")
print("HEAD:")
r = requests.head(good_url)
print(r.status_code, r.text)
# print("GET:")
# r = requests.get(good_url)
# print(r.status_code, r.text)

print("This one should fail\n========================\n")
print("HEAD:")
r = requests.head(bad_url)
print(r.status_code, r.text)
# print("GET:")
# r = requests.get(bad_url)
# print(r.status_code, r.text)

# url: 