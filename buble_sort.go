// Bubble Sort en Go (Golang) - Leer toda una carpeta de archivos de entrada

package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

func bubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}

func measureAndSaveTime(filename string, data []int) {
	// Asegurarse de que la carpeta exista antes de intentar guardar el archivo
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
		bubbleSort(arr)

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

	resultFileName := "go_resultados_bubble_sort/time_" + filepath.Base(filePath)
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
