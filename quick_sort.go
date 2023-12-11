// Quick Sort en Go (Golang)

package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

func quickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := arr[len(arr)/2]
	var left, middle, right []int

	for _, num := range arr {
		switch {
		case num < pivot:
			left = append(left, num)
		case num == pivot:
			middle = append(middle, num)
		case num > pivot:
			right = append(right, num)
		}
	}

	result := append(append(quickSort(left), middle...), quickSort(right)...)
	return result
}

func measureAndSaveTime(filename string, data []int) {
	err := os.MkdirAll(filepath.Dir(filename), os.ModePerm)
	if err != nil {
		panic(err)
	}

	file, err := os.Create(filename)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	for i := 0; i < 5; i++ {
		startTime := time.Now()

		arr := append([]int(nil), data...)
		_ = quickSort(arr)

		duration := time.Since(startTime).Seconds()

		file.WriteString(fmt.Sprintf("%d %.6f\n", len(data), duration))
	}
}

func processFile(filePath string) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		panic(err)
	}

	strValues := strings.Fields(string(content))
	data := make([]int, len(strValues))
	for i, strVal := range strValues {
		val, err := strconv.Atoi(strVal)
		if err != nil {
			panic(err)
		}
		data[i] = val
	}

	resultFileName := "go_resultados_quick_sort/time_" + filepath.Base(filePath)
	measureAndSaveTime(resultFileName, data)
}

func main() {
	inputFolder := "numeros_aleatorios"

	err := filepath.Walk(inputFolder, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() {
			return nil
		}
		processFile(path)
		return nil
	})
	if err != nil {
		panic(err)
	}
}
