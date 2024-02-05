import * as readline from 'readline';

let dexterity: number = 0
let wisdom: number = 0
let inteligence: number = 0
let perception: number = 0
let luck: number = 0
let strength: number = 0
let charisma: number = 0

let numero: number = 0

const user = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

user.question('digite o nome do seu pessonagem: ', (resposta) => {
    console.log("----------------------------")
    console.log(`\x1b[33m`, `nome: ${resposta}`);
    console.log("----------------------------")
    user.close();

    numberRandow(
        dexterity,
        wisdom,
        inteligence,
        perception,
        luck,
        strength,
        charisma,
    )

})

const numberRandow = (
    d: number,
    w: number,
    i: number,
    p: number,
    l: number,
    s: number,
    c: number,
) => {

    d = Math.floor(Math.random() * (20 - 4 + 1)) + 4;
    w = Math.floor(Math.random() * (20 - 4 + 1)) + 4;
    i = Math.floor(Math.random() * (20 - 4 + 1)) + 4;
    p = Math.floor(Math.random() * (20 - 4 + 1)) + 4;
    l = Math.floor(Math.random() * (20 - 4 + 1)) + 4;
    s = Math.floor(Math.random() * (20 - 4 + 1)) + 4;
    c = Math.floor(Math.random() * (20 - 4 + 1)) + 4;

    console.log(`\x1b[36m`, ` Destreza 🤸: ${d}`)
    console.log(`\x1b[36m`, ` Sabedoria 💫: ${w}`)
    console.log(`\x1b[36m`, ` Inteligência 🧠: ${i}`)
    console.log(`\x1b[36m`, ` Percepçao 👁️: ${l}`)
    console.log(`\x1b[36m`, ` Sorte 🍀: ${l}`)
    console.log(`\x1b[36m`, ` Força 💪 : ${s}`)
    console.log(`\x1b[36m`, ` Carisma 😍: ${c}`)
    console.log(`\x1b[33m`, "----------------------------")

}