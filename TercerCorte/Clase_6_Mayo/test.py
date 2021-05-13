import time
import simulador
import simuladorCython

def run_simulator(simulador):
    AU = (149.6e6 * 1000)
    sun = simulador.Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10**30

    earth = simulador.Body()
    earth.name = 'Earth'
    earth.mass = 5.9742 * 10**24
    earth.px = -1 * AU
    earth.vy = 29.783 * 1000

    venus = simulador.Body()
    venus.name = 'Venus'
    venus.mass = 4.8685 * 10**24
    venus.px = 0.723 * AU
    venus.vy = -35.02 * 1000

    simulador.loop([sun, earth, venus])   

def main():
    start = time.time()
    run_simulator(simulador)
    total_time = time.time() - start

    start = time.time()
    run_simulator(simuladorCython)
    cy_total_time = time.time() - start

    speedUp = round(total_time/cy_total_time, 3)
    print(f"Python time: {total_time} \n")
    print(f"Cython time: {cy_total_time} \n")
    print(f"SpeedUp: {speedUp} \n")


if __name__ == '__main__':
    main()