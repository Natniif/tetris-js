const Tshape = [
    [0, R, 0],
    [R, R, R],
];

const Lshape = [
    [B, 0],
    [B, 0],
    [B, B],
];

const Ishape = [[G], [G], [G]];

const SquareShape = [
    [Y, Y],
    [Y, Y],
];

function initGrid(rows, cols) {
    return Array.from({ length: rows }, () => Array(cols).fill(0));
}

function randomPiece() {
    const shapes = [Tshape, Lshape, Ishape, SquareShape];
    const randomIndex = Math.floor(Math.random() * shapes.length);

    return shapes[randomIndex];
}

function rotatePieceLeft(piece) {
    const rows = piece.length;
    const cols = piece[0].length;

    let newArray = Array.from({ length: cols }, () => Array(rows).fill(0));
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            newArray[j][i] = piece[i][j];
        }
    }

    return newArray;
}

function rotatePieceRight(piece) {
    const rows = piece.length;
    const cols = piece[0].length;

    let newArray = Array.from({ length: cols }, () => Array(rows).fill(0));
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            newArray[j][i] = piece[rows - i - 1][cols - j - 1]; // -1 to account for 0 indexing
        }
    }

    return new;
}

function createNewPiece(grid) {
    const piece = randomPiece();
    const xpos = Math.round((grid.length - piece.length) / 2);
    for (let i = 0; i < piece.length; i++) {
        for (let j = 0; j < piece[0].length; j++) {
            // end game if grid section is already 0
            if (grid[i + xpos][j] !== 0) {
                return false;
            }

            grid[i + xpos][j] = piece[i][j];
        }
    }
    return grid;
}

// turn letters lower cased when placed
function piecePlaced() {}

function fallOneBlock() {}

function movePiece() {}

function isTetris() {}

function tetris() {}

let grid = initGrid(15, 10);
const canvas = document.getElementsByClassName("tetris-board");
const context = canvas.getContext("2d");

const scoreElement = document.getElementById("scoreboard");
const score = 0;

function main() {
    do {
        if (piecePlaced()) {
            if (isTetris()) {
                tetris();
            }
            grid = createNewPiece(grid);
            scoreElement.textContent = "score: $(score)";
        }
        fallOneBlock();
    } while (!grid);

    // exit loop
    return false;
}

// loop
const interval = setInterval(function () {
    if (!main()) {
        clearInterval(interval);
    }
}, 100);

function testing() {
    piece = randomPiece();
    console.log(piece);
    console.log(rotatePieceRight(piece));
}
