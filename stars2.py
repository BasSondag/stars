def draw_stars(arr):
	for i in range(len(a)):
		if isinstance(arr[i],(int)):
			arr[i] *= "*"
			print arr[i]
		else:
			arr[i] = arr[i][0] * len(arr[i])
			arr[i] = arr[i].lower()
			print arr[i]
	return

a = [4,"Tom", 1, "michael", 5, 7, "jimmy Smith"]
draw_stars(a)