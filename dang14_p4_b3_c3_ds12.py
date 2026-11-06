import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang14_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(1,7)
                b=a*10
                c=nsimplify(b/2)
                f=(1/c)*x**2
                g=sqrt(c*x)
                k=(2/3)*sqrt(c)*x**(3/2)-(x**3)/(3*c)
                k1=k.subs(x,c)
                k2=k.subs(x,0)
                s=nsimplify(4*(k1-k2))
                number = Decimal(float(s))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                if (k1-k2)==int(k1-k2):
                    kqq='=%s'%(latex(nsimplify(4*(k1-k2))))
                else:
                    kqq='\\approx %s'%(latex(kq))
                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Trên một tấm bìa hình vuông cạnh $%s$ cm. Người thiết kế đã sử dụng bốn đường parabol có chung đỉnh tại tâm tấm bìa để tạo ra bốn cánh hoa (được tô màu như hình vẽ). Tính diện tích phần cánh hoa của tấm bìa (kết quả làm tròn đến hàng đơn vị).'
                            '}{'
                            '\\scalebox{0.6}{ '  
                            '\\begin{tikzpicture}[scale=1]\n'
                            '\\fill[red!30] plot[domain=0:3, samples=100, variable=\\x] (\\x,{sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({sqrt(3*\\y)},\\y) -- cycle;\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (\\x,{sqrt(3*\\x)});\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({sqrt(3*\\y)},\\y);\n'
                '\\fill[blue!30] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({-sqrt(3*\\y)},\\y) -- cycle;\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{sqrt(3*\\x)});\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({-sqrt(3*\\y)},\\y);\n'
                '\\fill[green!30] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{-sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({-sqrt(3*\\y)},-\\y) -- cycle;\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{-sqrt(3*\\x)});\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({-sqrt(3*\\y)},-\\y);\n'
                '\\fill[yellow!30] plot[domain=0:3, samples=100, variable=\\x] (\\x,{-sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({sqrt(3*\\y)},-\\y) -- cycle;\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (\\x,{-sqrt(3*\\x)});\n'
                '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({sqrt(3*\\y)},-\\y);\n'
                '\\draw[thick] (-3,-3) rectangle (3,3);\n'
                    '\\end{tikzpicture}}}\n'

                        %(latex(b)))

                # Nội dung lời giải
                loigiai = ('Chọn hệ trục tọa độ như hình vẽ\\\\ \n'
                        '\\begin{center}\n'
                        '\\begin{tikzpicture}[scale=0.6] \n'
                        '\\draw[->] (-4,0) -- (4,0) node[below] {$x$}; \n'
                        '\\draw[->] (0,-4) -- (0,4) node[left] {$y$}; \n'
                        '\\node at (0.2,-0.2) {$O$};\n'
                        '\\fill[red!30] plot[domain=0:3, samples=100, variable=\\x] (\\x,{sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({sqrt(3*\\y)},\\y) -- cycle;\n'
                        '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (\\x,{sqrt(3*\\x)});\n'
                            '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({sqrt(3*\\y)},\\y);\n'
                        '\\fill[blue!30] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({-sqrt(3*\\y)},\\y) -- cycle;\n'
                            '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{sqrt(3*\\x)});\n'
                            '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({-sqrt(3*\\y)},\\y);\n'
                        '\\fill[green!30] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{-sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({-sqrt(3*\\y)},-\\y) -- cycle;\n'
                            '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (-\\x,{-sqrt(3*\\x)});\n'
                        '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({-sqrt(3*\\y)},-\\y);\n'
                        '\\fill[yellow!30] plot[domain=0:3, samples=100, variable=\\x] (\\x,{-sqrt(3*\\x)}) -- plot[domain=3:0, samples=100, variable=\\y] ({sqrt(3*\\y)},-\\y) -- cycle;\n'
                        '\\draw[thick] plot[domain=0:3, samples=100, variable=\\x] (\\x,{-sqrt(3*\\x)});\n'
                            '\\draw[thick] plot[domain=0:3, samples=100, variable=\\y] ({sqrt(3*\\y)},-\\y);\n'
                        '\\draw[thick] (-3,-3) rectangle (3,3);\n'
                        '\\node at (3,0)[above right] {$%s$};\n'
                        '\\node at (0,3)[above right] {$%s$};\n'
                        '\\end{tikzpicture} \n'
                        '\\end{center}\n'
                        'Xác định parabol có bề lõm quay lên trên\\\\ \n'
                        'Gọi parabol có dạng $y=ax^2$. Vì parabol đi qua điểm $(%s;%s)$ nên $a=\\dfrac{1}{%s}$.\\\\ \n'
                        'Vậy $y=\\dfrac{1}{%s}x^2$.\\\\ \n'
                        'Xác định parabol có bề lõm quay sang phải\\\\ \n'
                        'Gọi parabol có dạng $y^2=px$. Vì parabol đi qua điểm $(%s;%s)$ nên $p=%s$.\\\\ \n'
                        'Suy ra $y^2=%sx$ nên đường parabol ở góc phần tư thứ nhất có dạng $y=\\sqrt{%sx}$.\\\\ \n'
                        'Diện tích cánh hoa ở góc phần tư thứ nhất là \\\\ \n'
                        '\\hspace*{1cm} $S=\\displaystyle\\int\\limits_{0}^{%s} \\left(\\sqrt{%sx}-\\dfrac{1}{%s}x^2\\right)\\text{d}x=%s$ cm$^2$.\\\\ \n'
                        'Vậy diện tích bốn cánh hoa là\\\\ \n'
                        '\\hspace*{1cm} $S\'=4\\cdot S=4\\cdot %s %s$ cm$^2$.'
                        %(latex(c),latex(c),latex(c),latex(c),latex(c),
                            latex(c),
                            latex(c),latex(c),latex(c),
                            latex(c), latex(c),
                            latex(c),latex(c),latex(c),
                            latex(nsimplify(k1-k2)),
                            latex(nsimplify(k1-k2)),kqq)
                        )


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

