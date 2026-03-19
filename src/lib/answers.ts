import answersRaw from '../../data/answers.json'

export interface WordEntry {
  word: string
  isPangram: boolean
  definition: string
  partOfSpeech: string
}

export interface DayAnswer {
  date: string
  centerLetter: string
  outerLetters: string[]
  pangrams: string[]
  words: WordEntry[]
}

const answers = answersRaw as DayAnswer[]

export function getAllAnswers(): DayAnswer[] {
  return answers.sort((a, b) => b.date.localeCompare(a.date))
}

export function getAnswerByDate(date: string): DayAnswer | undefined {
  return answers.find(d => d.date === date)
}

export function getTodayAnswer(): DayAnswer {
  const today = new Date().toISOString().split('T')[0]
  return answers.find(d => d.date === today) ?? answers[0]
}

export function formatDate(dateStr: string): string {
  return new Date(dateStr + 'T00:00:00').toLocaleDateString('en-US', {
    weekday: 'long', month: 'long', day: 'numeric', year: 'numeric',
  })
}
