from csv import writer

field_names = ['smoke_i', 'dis_i', 'dep_i', 'temp_i', 'hum_i', 'light_i']

with open('/home/ubuntu/Logs/logs.csv','a') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(field_names)
    f_object.close
