import { post } from '../utils'
import {
  AiOutlineExpand,
  AiOutlinePause,
  AiOutlineUndo,
  AiOutlineArrowDown,
  AiOutlineArrowUp,
  AiOutlineStepForward,
  AiOutlineStepBackward,
} from 'react-icons/ai'
import {
  RiVolumeDownLine,
  RiVolumeUpLine,
  RiArrowGoBackLine,
  RiArrowGoForwardLine,
} from 'react-icons/ri'
import { BiHide } from 'react-icons/Bi'

const SkipValue = ({ amount, isBackward }) => {
  const style = isBackward ? { right: '40px' } : { left: '40px' }
  return (
    <button
      className="footerButton"
      onClick={() => (isBackward ? post(['backward', amount]) : post(['forward', amount]))}
    >
      <div style={{ position: 'relative' }}>
        {isBackward ? <RiArrowGoBackLine size="45" /> : <RiArrowGoForwardLine size="45" />}
        <div className="skipText" style={style}>
          {amount}s
        </div>
      </div>
    </button>
  )
}

const Footer = () => {
  return (
    <div className="footer">
      <div className="footerRow">
        <SkipValue isBackward amount={30} />
        <SkipValue isBackward amount={5} />
        <SkipValue amount={5} />
        <SkipValue amount={30} />
      </div>
      <div className="footerRow">
        <button className="footerButton" onClick={() => post(['hide'])}>
          <BiHide size="40" />
        </button>
        <div className="buttonContainer">
          <button className="footerButton" onClick={() => post(['volumeup'])}>
            <RiVolumeUpLine size="30" />
          </button>
          <button className="footerButton" onClick={() => post(['volumedown'])}>
            <RiVolumeDownLine size="30" />
          </button>
        </div>
        <button className="footerButton" onClick={() => post(['prev'])}>
          <AiOutlineStepBackward size="40" />
        </button>
        <button className="footerButton" onClick={() => post(['next'])}>
          <AiOutlineStepForward size="40" textAnchor="COOL" />
        </button>
      </div>
      <div className="footerRow">
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
    </div>
  )
}

export default Footer
