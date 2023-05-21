from collections import deque
portions = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))
peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}
to_do_list = deque(peaks.keys())
conquered_peaks = []


for day in range(7):
    daily_total = portions.pop() + stamina.popleft()
    if to_do_list:
        if daily_total >= peaks[to_do_list[0]]:
            conquered_peaks.append(to_do_list.popleft())

if len(conquered_peaks) == len(peaks):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks:")
    print(*conquered_peaks, sep="\n")
