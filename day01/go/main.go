package main

import (
	"bufio"
	"fmt"
	"os"
)

type Rotation struct {
	Direction int
	Distance  int
}

func readInput() []Rotation {
	lines, err := readInputFromFile("day01/input.txt")
	if err != nil {
		panic(err)
	}
	rotations := []Rotation{}
	for _, line := range lines {
		var dirchar rune
		var dist int
		_, err := fmt.Sscanf(line, "%c%d", &dirchar, &dist)
		if err != nil {
			break
		}
		var dir int
		if dirchar == 'R' {
			dir = 1
		} else if dirchar == 'L' {
			dir = -1
		} else {
			panic(fmt.Sprintf("unknown direction char: %c", dirchar))
		}
		rotations = append(rotations, Rotation{Direction: dir, Distance: dist})
	}

	return rotations
}

func day1part1() {
	fmt.Println("day 1 part 1")
	rotations := readInput()
	n := 50
	password := 0
	for _, rot := range rotations {
		// fmt.Printf("Rotation: %+v\n", rot)
		n += rot.Direction * rot.Distance
		n = n % 100
		if n == 0 {
			password += 1
		}
	}
	fmt.Printf("password=%d\n", password)
}
func day1part2() {
	fmt.Println("day 1 part 2")
	rotations := readInput()
	n := 50
	password := 0
	for _, rot := range rotations {
		for i := 0; i < rot.Distance; i++ {
			// fmt.Printf("Rotation: %+v\n", rot)
			n += rot.Direction
			n = n % 100
			if n == 0 {
				password += 1
			}
		}
	}
	fmt.Printf("password=%d\n", password)
}

func main() {
	day1part1()
	day1part2()
}

func readInputFromFile(filename string) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}
