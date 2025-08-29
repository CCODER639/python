import time

def measure_time(mesurCo, start_time):
    if mesurCo == 0:
        start_time = time.time()
        mesurCo = 1
        return mesurCo, start_time, None
    else:
        stop_time = time.time()
        mesurCo = 0
        elapsed = stop_time - start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed - int(elapsed)) * 1000)
        output = f"{seconds:01d}.{milliseconds:02d}"
        print(output)
        return mesurCo, start_time, output

mesurCo = 0
start_time = 0

# Start timing
mesurCo, start_time, _ = measure_time(mesurCo, start_time)
input()
# Stop timing
mesurCo, start_time, output = measure_time(mesurCo, start_time)




