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


def bt_dang64_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số K là một bội số của 55 để kết quả P*K luôn là số nguyên
                K_list = [1100, 1650, 2200, 2750, 3190, 3300, 3850, 4400, 4950, 5500]
                K = random.choice(K_list)

                # Xác suất P = 32/55
                # kq = K * P
                kq = K * 32 // 55

                # Các đáp án trắc nghiệm nhiễu
                du = ['$%s$' % (latex(kq))]
                da = random.choice(du)
                s = [
                    '$%s$' % (latex(kq + 32)),
                    '$%s$' % (latex(kq - 32)),
                    '$%s$' % (latex(kq + 64)),
                    '$%s$' % (latex(kq - 64)),
                    '$%s$' % (latex(kq + 16)),
                    '$%s$' % (latex(kq - 16)),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi (Đã sửa bottom thành below)
                noidungcauhoi = ('''Một khung hình trang trí có dạng một đa giác đều $12$ cạnh $A_1A_2\\dots A_{12}$ (xem hình dưới) được gắn cố định trên một trần nhà. Bạn Dũng có $12$ bóng đèn gồm bốn bóng màu đỏ và tám bóng màu xanh, có công suất đôi một khác nhau. Bạn Dũng lắp ngẫu nhiên $12$ bóng đèn trên vào $12$ đỉnh $A_1, A_2, \\dots, A_{12}$ sao cho mỗi đỉnh có đúng một bóng đèn. Gọi $P$ là xác suất để mỗi hình vuông (có bốn đỉnh là các đỉnh của đa giác đã cho) đều có ít nhất một bóng đèn màu đỏ. Giá trị của $%sP$ bằng bao nhiêu?
            \\begin{center}
            \\begin{tikzpicture}[scale=1.5, line width=1pt]
            \\foreach \\i in {1,...,12} {
                \\coordinate (A\\i) at ({90 - (\\i-1)*30}:2);
                \\fill (A\\i) circle (1.5pt);}
            \\draw (A1) -- (A2) -- (A3) -- (A4) -- (A5) -- (A6) -- (A7) -- (A8) -- (A9) -- (A10) -- (A11) -- (A12) -- cycle;
            \\node[above] at (A1) {$A_1$};
            \\node[above right] at (A2) {$A_2$};
            \\node[right] at (A3) {$A_3$};
            \\node[right] at (A4) {$A_4$};
            \\node[below right] at (A5) {$A_5$};
            \\node[below] at (A6) {$A_6$};
            \\node[below] at (A7) {$A_7$};
            \\node[below left] at (A8) {$A_8$};
            \\node[left] at (A9) {$A_9$};
            \\node[left] at (A10) {$A_{10}$};
            \\node[above left] at (A11) {$A_{11}$};
            \\node[above left] at (A12) {$A_{12}$};
            \\draw[thin, gray] (A1) -- (A4) -- (A7) -- (A10) -- cycle;
            \\draw[thin, gray] (A2) -- (A5) -- (A8) -- (A11) -- cycle;
            \\draw[thin, gray] (A3) -- (A6) -- (A9) -- (A12) -- cycle;
            \\end{tikzpicture}
            \\end{center}''' % (latex(K)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Đa giác đều $12$ cạnh có $\\frac{12}{4} = 3$ hình vuông có các đỉnh là đỉnh của đa giác. \\\\
            Không gian mẫu là số cách xếp $12$ bóng đèn đôi một khác nhau vào $12$ đỉnh: $n(\\Omega) = 12!$. \\\\
            Gọi biến cố $E$: "Mỗi hình vuông đều có ít nhất một bóng đèn màu đỏ". \\\\
            Để biến cố $E$ xảy ra, ta cần chọn $4$ vị trí đỉnh cho $4$ bóng đèn đỏ sao cho trong $3$ hình vuông, mỗi hình vuông có ít nhất một bóng đèn đỏ. \\\\
            Vì chỉ có $4$ bóng đèn đỏ phân bố vào $3$ hình vuông nên số lượng bóng đèn đỏ trên $3$ hình vuông này bắt buộc phải là $(2, 1, 1)$ (tức là $1$ hình vuông có $2$ bóng đỏ, $2$ hình vuông còn lại mỗi hình vuông có $1$ bóng đỏ). \\\\
            Số cách chọn hình vuông có chứa $2$ bóng đèn đỏ là: $C_3^1 = 3$ cách. \\\\
            Số cách chọn $2$ đỉnh trên hình vuông đó để đặt bóng đỏ là: $C_4^2 = 6$ cách. \\\\
            Số cách chọn $1$ đỉnh trên mỗi hình vuông trong $2$ hình vuông còn lại để đặt bóng đỏ là: $C_4^1 \\cdot C_4^1 = 16$ cách. \\\\
            Sau khi đã chọn được $4$ vị trí, số cách xếp $4$ bóng đỏ vào $4$ vị trí đó là: $4!$ cách. \\\\
            Số cách xếp $8$ bóng xanh vào $8$ vị trí còn lại là: $8!$ cách. \\\\
            Suy ra số kết quả thuận lợi cho biến cố $E$ là: $n(E) = 3 \\cdot 6 \\cdot 16 \\cdot 4! \\cdot 8! = 288 \\cdot 4! \\cdot 8!$. \\\\
            Xác suất của biến cố $E$ là: $P = \\frac{n(E)}{n(\\Omega)} = \\frac{288 \\cdot 4! \\cdot 8!}{12!} = \\frac{288}{C_{12}^4} = \\frac{288}{495} = \\frac{32}{55}$. \\\\
            Vậy giá trị cần tìm là: $%sP = %s \\cdot \\frac{32}{55} = %s$.'''
                           % (latex(K), latex(K), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

