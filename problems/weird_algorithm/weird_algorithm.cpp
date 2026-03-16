#include <iostream>
#include <algorithm>
#include <chrono>
#include <cmath>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

struct Cell {
    int row, col;
};

constexpr int MAX_N = 205;
constexpr int MAX_N2 = MAX_N * MAX_N;
constexpr double TIME_LIMIT = 2.85;
constexpr double TEMP_INITIAL = 2e9;
constexpr double TEMP_MIN = 0.5;
constexpr int CHECK_INTERVAL = 1 << 12;

int  N, N2;
int  A[MAX_N][MAX_N];
Cell path[MAX_N2];
int  pathPos[MAX_N][MAX_N];
int  flatA[MAX_N2];
ll   prefA[MAX_N2 + 1];

ull rng_state = 987654321098765ULL;
inline ull xnext() {
    rng_state ^= rng_state << 13;
    rng_state ^= rng_state >> 7;
    rng_state ^= rng_state << 17;
    return rng_state;
}

inline bool areKingNeighbors(Cell a, Cell b) {
    return max(abs(a.row - b.row), abs(a.col - b.col)) == 1;
}

inline bool inBounds(int r, int c) {
    return (unsigned)r < (unsigned)N && (unsigned)c < (unsigned)N;
}

void buildSnakePath() {
    int k = 0;
    for (int i = 0; i < N; i++) {
        if (i % 2 == 0)
            for (int j = 0;   j < N;  j++) path[k] = {i, j}, pathPos[i][j] = k++;
        else
            for (int j = N-1; j >= 0; j--) path[k] = {i, j}, pathPos[i][j] = k++;
    }
}

void initArrays() {
    ll acc = 0;
    prefA[0] = 0;
    for (int k = 0; k < N2; k++) {
        flatA[k]     = A[path[k].row][path[k].col];
        acc         += flatA[k];
        prefA[k + 1] = acc;
    }
}

inline ll scoreDelta(int l, int r) {
    ll sumA  = prefA[r + 1] - prefA[l];
    ll sumKA = 0;
    for (int k = l; k <= r; ++k)
        sumKA += (ll)k * flatA[k];
    return (ll)(l + r) * sumA - 2LL * sumKA;
}

inline void applyReversal(int l, int r) {
    for (int a = l, b = r; a < b; ++a, --b) {
        swap(path[a],  path[b]);
        pathPos[path[a].row][path[a].col] = a;
        pathPos[path[b].row][path[b].col] = b;
        swap(flatA[a], flatA[b]);
    }
}

int pickRightBound(int l) {
    int cands[8], nc = 0;

    if (l == 0) {
        Cell pivot = path[0];
        for (int di = -1; di <= 1; ++di)
        for (int dj = -1; dj <= 1; ++dj) {
            if (!di && !dj) continue;
            int ni = pivot.row + di, nj = pivot.col + dj;
            if (!inBounds(ni, nj)) continue;
            int r = pathPos[ni][nj] - 1;
            if (r > 0) cands[nc++] = r;
        }
    } else {
        Cell pivot = path[l - 1];
        for (int di = -1; di <= 1; ++di)
        for (int dj = -1; dj <= 1; ++dj) {
            if (!di && !dj) continue;
            int ni = pivot.row + di, nj = pivot.col + dj;
            if (!inBounds(ni, nj)) continue;
            int r = pathPos[ni][nj];
            if (r <= l) continue;
            if (r < N2 - 1 && !areKingNeighbors(path[l], path[r + 1])) continue;
            cands[nc++] = r;
        }
    }

    if (!nc) return -1;
    return cands[xnext() % (ull)nc];
}

void simulatedOtschig() {
    auto t0 = chrono::steady_clock::now();
    double temperature = TEMP_INITIAL;
    initArrays();

    for (int iter = 0; ; ++iter) {
        if ((iter & (CHECK_INTERVAL - 1)) == 0) {
            double elapsed = chrono::duration<double>(
                chrono::steady_clock::now() - t0).count();
            if (elapsed >= TIME_LIMIT) break;
            // Исправлено: теперь T → TEMP_MIN, а не T → 1
            temperature = TEMP_INITIAL *
                pow(TEMP_MIN / TEMP_INITIAL, elapsed / TIME_LIMIT);
        }

        int l = (int)(xnext() % (ull)(N2 - 1));
        int r = pickRightBound(l);
        if (r <= l) continue;

        ll delta = scoreDelta(l, r);

        bool accept;
        if (delta >= 0) {
            accept = true;
        } else if (temperature <= TEMP_MIN) {
            accept = false;
        } else {
            double prob = exp((double)delta / temperature);
            accept = (xnext() >> 33) < (ull)(prob * (double)(1u << 31));
        }

        if (accept) applyReversal(l, r);
    }
}

void readInput() {
    std::cin >> N; N2 = N * N;

    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            std::cin >> A[i][j];
}

void printPath() {
    for (int k = 0; k < N2; ++k)
        std::cout << path[k].row << ' ' << path[k].col << '\n';
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    readInput();
    buildSnakePath();
    simulatedOtschig();
    printPath();

    return 0;
}