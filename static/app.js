
const taskList = document.getElementById("task-list");
const taskCount = document.getElementById("task-count");
const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const message = document.getElementById("message");

let tasks = [];

function renderTasks() {
    taskList.replaceChildren();

    tasks.forEach((task) => {
        const item = document.createElement("li");
        item.textContent = task.title;
        taskList.appendChild(item);
    });

    taskCount.textContent = `${tasks.length} görev`;
}

async function loadTasks() {
    try {
        const response = await fetch("/tasks");

        if (!response.ok) {
            throw new Error("Görevler alınamadı.");
        }

        tasks = await response.json();
        renderTasks();
    } catch (error) {
        message.textContent = "Görevler yüklenemedi.";
        console.error(error);
    }
}

taskForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = taskInput.value.trim();

    if (!title) {
        return;
    }

    const button = taskForm.querySelector("button");
    button.disabled = true;
    message.textContent = "Görev kaydediliyor...";

    try {
        const response = await fetch("/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Görev kaydedilemedi.");
        }

        taskInput.value = "";
        message.textContent = "Görev PostgreSQL'e kaydedildi.";
        await loadTasks();
    } catch (error) {
        message.textContent = error.message;
    } finally {
        button.disabled = false;
    }
});

loadTasks();
