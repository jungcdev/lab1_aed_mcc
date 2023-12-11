#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <chrono>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

// Función para implementar el algoritmo de Quick Sort
vector<int> quickSort(vector<int>& arr) {
    if (arr.size() <= 1) {
        return arr;
    }

    int pivot = arr[arr.size() / 2];
    vector<int> left, middle, right;

    for (int num : arr) {
        if (num < pivot) {
            left.push_back(num);
        } else if (num == pivot) {
            middle.push_back(num);
        } else {
            right.push_back(num);
        }
    }

    vector<int> result;
    result.reserve(arr.size());

    vector<int> sortedLeft = quickSort(left);
    vector<int> sortedRight = quickSort(right);

    result.insert(result.end(), sortedLeft.begin(), sortedLeft.end());
    result.insert(result.end(), middle.begin(), middle.end());
    result.insert(result.end(), sortedRight.begin(), sortedRight.end());

    return result;
}

// Función para medir el tiempo de ejecución y guardar los resultados en un archivo
void measureAndSaveTime(const string& filename, const vector<int>& data) {
    ofstream outfile(filename);
    for (int i = 0; i < 5; ++i) {
        auto start_time = chrono::high_resolution_clock::now();

        // Clonamos el vector antes de ordenar para mantener los datos originales en cada ejecución
        vector<int> arr = data;
        arr = quickSort(arr);

        auto end_time = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end_time - start_time);

        outfile << data.size() << " " << fixed << setprecision(6) << duration.count() / 1e6 << endl;
    }
    outfile.close();
}

int main() {
    const string inputFolder = "numeros_aleatorios";
    const string resultadosFolder = "cpp_resultados_quick_sort";

    // Verificar y crear la carpeta de resultados si no existe
    if (!fs::exists(resultadosFolder)) {
        fs::create_directory(resultadosFolder);
    }

    for (const auto& entry : fs::directory_iterator(inputFolder)) {
        if (entry.is_regular_file()) {
            ifstream infile(entry.path());
            vector<int> data;

            int num;
            while (infile >> num) {
                data.push_back(num);
            }

            infile.close();

            // Medir el tiempo y guardar los resultados en un archivo
            string resultFileName = resultadosFolder + "/time_" + entry.path().filename().string();
            measureAndSaveTime(resultFileName, data);
        }
    }

    return 0;
}
