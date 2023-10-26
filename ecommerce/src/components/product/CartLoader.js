import React from "react"
import ContentLoader from "react-content-loader"

const MyLoader = (props) => (
  <ContentLoader
    speed={2}
    width={350}
    height={350}
    viewBox="0 0 400 460"
    backgroundColor="#f3f3f3"
    foregroundColor="#ecebeb"
    {...props}
  >
    <rect x="4" y="329" rx="2" ry="2" width="168" height="12" />
    <rect x="182" y="486" rx="2" ry="2" width="140" height="10" />
    <rect x="4" y="6" rx="2" ry="2" width="318" height="315" />
  </ContentLoader>
)

export default MyLoader

