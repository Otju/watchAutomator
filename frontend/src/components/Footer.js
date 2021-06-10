import { post } from '../utils'
import {
  AiOutlineExpand,
  AiOutlinePause,
  AiOutlineUndo,
  AiOutlineArrowDown,
  AiOutlineArrowUp,
} from 'react-icons/ai'

const Footer = () => {
  return (
    <div className="footer">
      <button className="footerButton" onClick={() => post(['fullscreen'])}>
        <AiOutlineExpand size="40" />
      </button>
      <button className="footerButton" onClick={() => post(['pause'])}>
        <AiOutlinePause size="40" />
      </button>
      <button className="footerButton" onClick={() => post(['refresh'])}>
        <AiOutlineUndo size="40" />
      </button>
      <div className="buttonContainer">
        <button className="footerButton" onClick={() => post(['scrollup'])}>
          <AiOutlineArrowUp size="30" />
        </button>
        <button className="footerButton" onClick={() => post(['scrolldown'])}>
          <AiOutlineArrowDown size="30" />
        </button>
      </div>
    </div>
  )
}

export default Footer
