import time

start = time.time()

dec_string = ""
i = 1
while len(dec_string) < 1000000:
    dec_string += str(i)
    i += 1

print(int(dec_string[0]) * int(dec_string[9]) * int(dec_string[99]) * int(dec_string[999]) * int(dec_string[9999])
      * int(dec_string[99999]) * int(dec_string[999999]))
print("Process took", time.time() - start, "sec")
