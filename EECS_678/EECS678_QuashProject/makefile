run:	
	make quash
	./quash

valgrind:
	make quash
	valgrind --leak-check=full --show-leak-kinds=all ./quash

quash: main.cpp quash_func.cpp quash_listener.cpp
	g++ -std=c++20 -Wall -g main.cpp quash_func.cpp quash_listener.cpp -o quash

clean:
	rm -f quash
	rm -f *.txt