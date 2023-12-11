#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <chrono>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

// Función para implementar el algoritmo de Merge Sort
vector<int> merge(vector<int>& left, vector<int>& right) {
    vector<int> result;
    int i = 0, j = 0;

    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }

    while (i < left.size()) {
        result.push_back(left[i]);
        i++;
    }

    while (j < right.size()) {
        result.push_back(right[j]);
        j++;
    }

    return result;
}

// Función para implementar el algoritmo de Merge Sort
vector<int> mergeSort(vector<int>& arr) {
    if (arr.size() <= 1) {
        return arr;
    }

    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    left = mergeSort(left);
    right = mergeSort(right);

    return merge(left, right);
}

// Función para medir el tiempo de ejecución y guardar los resultados en un archivo
void measureAndSaveTime(const string& filename, const vector<int>& data) {
    ofstream outfile(filename);
    for (int i = 0; i < 5; ++i) {
        auto start_time = chrono::high_resolution_clock::now();

        // Clonamos el vector antes de ordenar para mantener los datos originales en cada ejecución
        vector<int> arr = data;
        arr = mergeSort(arr);

        auto end_time = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end_time - start_time);

        outfile << data.size() << " " << fixed << setprecision(6) << duration.count() / 1e6 << endl;
    }
    outfile.close();
}

int main() {
    const string inputFolder = "numeros_aleatorios";
    const string resultadosFolder = "cpp_resultados_merge_sort";

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
