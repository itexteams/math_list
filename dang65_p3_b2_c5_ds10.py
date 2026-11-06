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


def bt_dang65_p3_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                m = random.randint(4, 7)
                n = random.randint(4, 7)
                A = random.randint(2, 9)

                S = 6 * (2**m) + 6 * (2**n) - 24
                kq_int = A * S
                kq = str(kq_int)

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq),
                      ]
                da= random.choice(du)
                s = ['$%s$'%(latex(kq_int + A)),
                     '$%s$'%(latex(kq_int - A)),
                     '$%s$'%(latex(kq_int + 2*A)),
                     '$%s$'%(latex(kq_int - 2*A)),
                     '$%s$'%(latex(kq_int + 3*A)),
                     '$%s$'%(latex(kq_int - 3*A)),
                     '$%s$'%(latex(A * (6 * (2**m) + 6 * (2**n))))
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('''Cho bảng $%s \\times %s$ gồm $%s$ ô vuông đơn vị và cho bốn màu. Người ta tô mỗi ô trong bảng bởi một trong bốn màu đã cho sao cho hai ô bất kì có chung đỉnh hoặc chung cạnh thì khác màu. Hai cách tô màu bảng được gọi là giống nhau nếu mỗi ô của bảng có cùng màu ở cả hai cách tô (không tính đến thứ tự tô màu các ô). Gọi $S$ là số cách tô màu bảng phân biệt thỏa mãn điều kiện trên. Giá trị của $%s S$ bằng bao nhiêu?'''
                                 %(latex(m), latex(n), latex(m*n), latex(A)
                                 ))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải có chèn hình bằng TikZ (minh họa bảng 4x4)
                loigiai=('''Điều kiện hai ô chung đỉnh hoặc chung cạnh khác màu tương đương với việc mọi hình vuông kích thước $2 \\times 2$ trên bảng đều chứa $4$ màu phân biệt. \\\\
                         Chia $4$ màu thành $2$ tập hợp, mỗi tập gồm $2$ màu. Có $\\frac{C_4^2}{2} = 3$ cách phân hoạch. \\\\
                         \\begin{center}
                         \\begin{tikzpicture}[scale=0.8, line width=1pt]
                         \\draw (0,0) grid (4,4);
                         \\node at (0.5,3.5) {$1$}; \\node at (1.5,3.5) {$2$}; \\node at (2.5,3.5) {$1$}; \\node at (3.5,3.5) {$2$};
                         \\node at (0.5,2.5) {$3$}; \\node at (1.5,2.5) {$4$}; \\node at (2.5,2.5) {$3$}; \\node at (3.5,2.5) {$4$};
                         \\node at (0.5,1.5) {$2$}; \\node at (1.5,1.5) {$1$}; \\node at (2.5,1.5) {$2$}; \\node at (3.5,1.5) {$1$};
                         \\node at (0.5,0.5) {$4$}; \\node at (1.5,0.5) {$3$}; \\node at (2.5,0.5) {$4$}; \\node at (3.5,0.5) {$3$};
                         \\node at (2,-0.5) {Minh họa một cách tô thuộc Trường hợp 1};
                         \\end{tikzpicture}
                         \\end{center}
                         Mỗi cách tô thỏa mãn điều kiện sẽ rơi vào một trong hai trường hợp sau: \\\\
                         Trường hợp 1: Các hàng luân phiên sử dụng $2$ tập màu. Có $3 \\cdot 2 = 6$ cách gán các tập màu cho các hàng. Mỗi hàng có $2$ cách luân phiên tô màu. Do bảng có $%s$ hàng nên số cách tô ở trường hợp này là $6 \\cdot 2^{%s}$. \\\\
                         Trường hợp 2: Các cột luân phiên sử dụng $2$ tập màu. Lập luận tương tự, do bảng có $%s$ cột nên số cách tô là $6 \\cdot 2^{%s}$. \\\\
                         Trường hợp giao nhau: Cả hàng và cột đều luân phiên sử dụng các tập màu. Khi đó, toàn bộ bảng được xác định duy nhất bởi cách tô $4$ ô vuông góc trên cùng bên trái. Số cách tô phần giao nhau chính là số cách tô một hình vuông $2 \\times 2$ bằng $4$ màu phân biệt, và bằng $4! = 24$ cách. \\\\
                         Vậy số cách tô bảng thỏa mãn là $S = 6 \\cdot 2^{%s} + 6 \\cdot 2^{%s} - 24 = %s$. \\\\
                         Giá trị cần tìm là $%s S = %s \\cdot %s = %s$.'''
                         %(latex(m), latex(m), latex(n), latex(n), latex(m), latex(n), latex(S), latex(A), latex(A), latex(S), latex(kq_int)
                         ))

            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_int))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n' + dapan +
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

