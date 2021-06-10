import { useEffect, useState } from 'preact/hooks'
import { post, get } from '../utils'

const NumberSelect = ({ type, selectedIndex }) => {
  const [dropdownValues, setDropDownValues] = useState(null)

  useEffect(() => {
    get(type).then((res) => {
      const count = res.count
      let array = Array.from(Array(count).keys())
      array = array.map((item) => item + 1)
      setDropDownValues(array)
    })
  }, [selectedIndex])

  return (
    <div className="numberSelect">
      {dropdownValues &&
        dropdownValues.map((value) => (
          <button
            value={value}
            onClick={() => post(['select', type, value])}
            className="selectButton"
          >
            {value}
          </button>
        ))}
    </div>
  )
}

const ItemSelect = ({ handler, saved, setSaved }) => {
  const handleDelete = (value) => {
    post(['delete', value])
    setSaved(saved.filter((item) => item !== value))
  }

  return (
    <div className="itemSelect">
      {saved &&
        saved.map((value) => (
          <div className="item">
            <button value={value} onClick={() => handler(value)} className="itemButton">
              {value}
            </button>
            <button className="deleteButton" onClick={() => handleDelete(value)} type="button">
              ✖
            </button>
          </div>
        ))}
    </div>
  )
}

const Main = () => {
  const [selectedIndex, setSelectedIndex] = useState(3)
  const [text, setText] = useState('')
  const [saved, setSaved] = useState([])

  const handleSearch = (event) => {
    event.preventDefault()
    post(['search', text.replace(' ', '+')])
  }

  useEffect(() => {
    get('save').then((res) => {
      const keys = Object.keys(res)
      setSaved(keys)
    })
  }, [])

  const handleSave = (event) => {
    event.preventDefault()
    post(['save', text.replace(' ', '+')])
    setText('')
    setSelectedIndex(4)
    setSaved([...saved, text])
  }

  const fields = [
    {
      name: 'Search',
      content: (
        <form onSubmit={handleSearch}>
          <input type="text" onChange={(event) => setText(event.target.value)} value={text} />
          <button type="submit">Search</button>
        </form>
      ),
    },
    {
      name: 'Select show',
      content: <NumberSelect type="show" selectedIndex={selectedIndex} />,
    },
    {
      name: 'Select episode',
      content: <NumberSelect type="episode" selectedIndex={selectedIndex} />,
    },
    {
      name: 'Continue',
      content: (
        <ItemSelect
          saved={saved}
          setSaved={setSaved}
          handler={(value) => post(['continue', value.replace(' ', '+')])}
        />
      ),
    },
    {
      name: 'Save',
      content: (
        <>
          <div>
            <form onSubmit={handleSave}>
              <input type="text" onChange={(event) => setText(event.target.value)} value={text} />
              <button type="submit">+</button>
            </form>
          </div>
          <div>
            <ItemSelect
              saved={saved}
              setSaved={setSaved}
              handler={(value) => post(['save', value.replace(' ', '+')])}
            />
          </div>
        </>
      ),
    },
  ]

  useEffect(() => {
    const field = fields[selectedIndex]
    if (field.onSelect) {
      field.onSelect()
    }
  }, [selectedIndex])

  return (
    <>
      <div className="topBar">
        {fields.map(({ name }, i) => {
          const isSelected = selectedIndex === i
          return (
            <button
              className="footerButton"
              onClick={() => setSelectedIndex(i)}
              style={{ color: isSelected ? 'red' : 'white' }}
            >
              {name}
            </button>
          )
        })}
      </div>
      <div id="main">{fields[selectedIndex].content}</div>
    </>
  )
}

export default Main
