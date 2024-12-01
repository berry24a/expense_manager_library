from setuptools import setup, find_packages

setup(
    name="expense_manager_library",
    version="1.0.0",
    packages=find_packages(),  # 현재 디렉토리와 서브 디렉토리의 모든 패키지를 탐색
    install_requires=[
        "pandas>=1.0.0",
    ],
    include_package_data=True,
    description="Library for categorizing and managing expense data",
)
