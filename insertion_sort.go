// Insertion Sort en Go (Golang)

package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

func insertionSort(arr []int) {
	for i := 1; i < len(arr); i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && key < arr[j] {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
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
		insertionSort(arr)

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

	resultFileName := "go_resultados_insertion_sort/time_" + filepath.Base(filePath)
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
