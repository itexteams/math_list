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


def bt_dang70_p1_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bước 3: Random các hệ số của Parabol: y = Ax^2 + Bx + C
                # Để đơn giản và giống mẫu, ta đặt Parabol dạng: y = a_p*x^2 - 4(k*m - n)x + (8*k^2*m^2 - C_const)
                # Ở đây tôi sẽ random các giá trị cơ bản để đảm bảo bài toán luôn có nghiệm đẹp

                a_p = randint(1, 3) # Hệ số a của Parabol (trong ảnh là 2)
                k = randint(1, 3)   # Hệ số k trong cụm (km - n) (trong ảnh là 2)
                n = randint(1, 5)   # Hệ số n trong cụm (km - n) (trong ảnh là 1)
                c_const = randint(1, 5) # Hệ số tự do trừ đi (trong ảnh là 3)

                # Biểu thức Parabol: y = a_p*x^2 - 4(k*m - n)x + (2*a_p*k^2*m^2 - c_const)
                # Lưu ý: Để triệt tiêu m^2 trong Delta, hệ số của m^2 ở hằng số phải là (4*k)^2 / (4*a_p) = 4*k^2/a_p * a_p... 
                # Tính toán để Delta chỉ còn m bậc 1: 
                # Delta = [4(km-n)+a]^2 - 4*a_p*( (4*k^2/a_p)*m^2 - c_const - b )

                coeff_m2 = (4 * k**2) // a_p # Đảm bảo chia hết để ra số nguyên
                m_sq_term = coeff_m2 * a_p * 2 # Để giống mẫu 8m^2 với a_p=2, k=2 -> (4*4)/2 = 8

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Parabol $y = %sx^2 - 4(%sm - %s)x + %sm^2 - %s$ luôn tiếp xúc với đường thẳng nào sau đây?'''
                                 %(latex(a_p), latex(k), latex(n), latex(m_sq_term), latex(c_const)))

                # Tính toán đáp án đúng: a = 4*k, b = -c_const
                # Giải thích: Delta = (4km - 4n + a)^2 - 8a_p(m_sq_term/a_p * m^2 - c_const - b)
                # Để triệt tiêu m^2: (4k)^2 = 4 * a_p * (m_sq_term) => 16k^2 = 4 * a_p * (4k^2/a_p) (luôn đúng)

                final_a = 4 * k
                final_b = -c_const
                da_dung_str = 'y = %sx - %s' % (latex(final_a), latex(c_const)) if final_b < 0 else 'y = %sx + %s' % (latex(final_a), latex(final_b))

                # Bước 4: Điều chỉnh các phương án sai
                du = ['$%s$' % da_dung_str]
                da = du[0]

                s = [
                    '$y = %sx + %s$' % (latex(final_a + 1), latex(final_b)),
                    '$y = %sx - %s$' % (latex(final_a), latex(c_const + 2)),
                    '$y = %sx + %s$' % (latex(final_a - 2), latex(final_b + 1)),
                    '$y = %sx + %s$' % (latex(final_a), latex(final_b + 5)),
                    '$y = %sx - %s$' % (latex(final_a + 2), latex(c_const)),
                ]

                # Loại bỏ nếu trùng đáp án đúng (đề phòng random)
                if da in s: s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Nội dung lời giải chi tiết
                loigiai = (r'''Gọi $y = ax + b$ là đường thẳng mà parabol luôn tiếp xúc. \\
                           Phương trình hoành độ giao điểm $%sx^2 - 4(%sm - %s)x + %sm^2 - %s = ax + b$ \\
                           $\Leftrightarrow %sx^2 - (%sm - %s + a)x + %sm^2 - %s - b = 0. \quad (1)$ \\
                           Yêu cầu bài toán $\Leftrightarrow$ phương trình (1) luôn có nghiệm kép với mọi $m$ \\
                           $\Leftrightarrow \Delta = (%sm - %s + a)^2 - %s(%sm^2 - %s - b) = 0, \text{ với mọi } m$ \\
                           $\Leftrightarrow %s(%s + a)m + (%s + a)^2 + %s(%s + b) = 0, \text{ với mọi } m$ \\
                           $\Leftrightarrow \begin{cases} %s + a = 0 \\ (%s + a)^2 + %s(%s + b) = 0 \end{cases} \Leftrightarrow \begin{cases} a = %s \\ b = %s \end{cases}.$ \\
                           Vậy parabol luôn tiếp xúc với đường thẳng %s.'''
                           %(latex(a_p), latex(k), latex(n), latex(m_sq_term), latex(c_const),
                             latex(a_p), latex(4*k), latex(4*n), latex(m_sq_term), latex(c_const),
                             latex(4*k), latex(4*n), latex(4*a_p), latex(m_sq_term//a_p), latex(c_const),
                             latex(8*4*k), latex(-4*n), latex(-4*n), latex(4*a_p), latex(c_const),
                             latex(-4*n), latex(-4*n), latex(4*a_p), latex(c_const),
                             latex(final_a), latex(final_b), da))

                # Đưa các đáp án vào danh sách
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

