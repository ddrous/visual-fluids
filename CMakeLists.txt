cmake_minimum_required(VERSION 3.0.0)
project(NeuralFluids VERSION 0.1.0)

include(CTest)
enable_testing()

# add the MathFunctions library
# add_subdirectory(oneTBB)
add_subdirectory(mantaflow)

add_executable(NeuralFluids main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
