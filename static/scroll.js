let currentPage = 0

const nextPage = () => {
	console.log('nextPage')
	currentPage++
	const page = document.querySelector(`.page-${currentPage}`)
	page.scrollIntoView({ behavior: 'smooth' })
}

const prevPage = () => {
	console.log('prevPage')
	currentPage--
	const page = document.querySelector(`.page-${currentPage}`)
	page.scrollIntoView({ behavior: 'smooth' })
}