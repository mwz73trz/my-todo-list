import { Link } from "react-router-dom"

export default function Category(this.props) {
  return (
    <div>
      <Link to={`categories/${props.category.id}`}>{props.category.name}</Link>
    </div>
  )
}
