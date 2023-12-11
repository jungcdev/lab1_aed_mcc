#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <filesystem> 

using namespace std;
namespace fs = filesystem;

// Función para implementar el algoritmo de Bubble Sort
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void measureAndSaveTime(const string& filename, const vector<int>& data) {
    ofstream outfile(filename);
    for (int i = 0; i < 5; ++i) {
        auto start_time = chrono::high_resolution_clock::now();

        // Clonamos el vector antes de ordenar para mantener los datos originales en cada ejecución
        vector<int> arr = data;
        bubbleSort(arr);

        auto end_time = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::microseconds>(end_time - start_time);

        outfile << data.size() << " " << fixed << setprecision(6) << duration.count() / 1e6 << endl;
    }
    outfile.close();
}

int main() {
    const string inputFolder = "numeros_aleatorios";
    const string resultadosFolder = "cpp_resultados_buble_sort";

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