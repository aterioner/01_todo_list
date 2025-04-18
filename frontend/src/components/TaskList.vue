<template>
    <div class="container py-4 bg-light min-vh-100">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="card shadow-sm">
            <div class="card-body">
              <h3 class="card-title mb-4 text-center">📝 To-do List</h3>
  
              <!-- FORMULÁŘ NA PŘIDÁNÍ ÚKOLU -->
              <form @submit.prevent="addTask" class="mb-4 d-flex gap-2">
                <input
                  type="text"
                  class="form-control"
                  placeholder="Zadej nový úkol..."
                  v-model="newTaskTitle"
                />
                <button class="btn btn-primary" :disabled="!newTaskTitle.trim()">
                  Přidat
                </button>
              </form>
  
              <!-- SEZNAM ÚKOLŮ -->
              <ul class="list-group">
                <li
                  v-for="task in tasks"
                  :key="task.id"
                  class="list-group-item d-flex justify-content-between align-items-center"
                >
                  <label class="form-check-label d-flex align-items-center w-100">
                    <input
                      type="checkbox"
                      class="form-check-input me-2"
                      v-model="task.completed"
                      @change="updateTask(task)"
                    />
                    <span :class="{ 'text-decoration-line-through text-muted': task.completed }">
                      {{ task.title }}
                    </span>
                    <span class="ms-auto text-muted small">
                      {{ formatDate(task.created) }}
                    </span>
                  </label>
                  <button
                    class="btn btn-danger btn-sm btn-square d-flex align-items-center justify-content-center ms-2"
                    @click="deleteTask(task.id)"
                    title="Smazat úkol"
                  >
                    &times;
                  </button>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const tasks = ref([])
const newTaskTitle = ref('')
const API = 'https://todo-backend-4ycu.onrender.com'

// Načtení úkolů při načtení komponenty
onMounted(async () => {
  const response = await axios.get(`${API}/api/tasks/`)
  tasks.value = response.data
})

// Přidání nového úkolu s ošetřením chyby
const addTask = async () => {
  const trimmed = newTaskTitle.value.trim()
  if (!trimmed) return

  try {
    const response = await axios.post(
      `${API}/api/tasks/`,
      {
        title: trimmed,
        completed: false,
      },
    )
    tasks.value.unshift(response.data)
    newTaskTitle.value = ''
  } catch (error) {
    console.error('CHYBA PŘI POSTU:', error.response?.data || error.message)
  }
}

// Aktualizace úkolu (např. checkbox)
const updateTask = async (task) => {
  try {
    await axios.put(
      `${API}/api/tasks/${task.id}/`,
      task,
    )
  } catch (error) {
    console.error('CHYBA PŘI UPDATE:', error.response?.data || error.message)
  }
}

// Smazání úkolu
const deleteTask = async (id) => {
  try {
    await axios.delete(`${API}/api/tasks/${id}/`)
    tasks.value = tasks.value.filter(task => task.id !== id)
  } catch (error) {
    console.error('CHYBA PŘI DELETE:', error.response?.data || error.message)
  }
}

// Formátování data
const formatDate = (isoString) => {
  const date = new Date(isoString)
  return date.toLocaleString('cs-CZ', {
    day: '2-digit',
    month: '2-digit',
    year: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  })
}
</script>