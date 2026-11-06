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


def bt_dang30_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Phương án đúng (có tiệm cận đứng, dạng y = (ax+b)/(cx+d) với nghiệm mẫu không làm triệt tiêu tử)
                d = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                a = random.choice([-3, -2, -1, 1, 2, 3])
                b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                # Đảm bảo nghiệm của mẫu (-d) không phải là nghiệm của tử
                while a*(-d) + b == 0:
                    b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

                num_d = a*x + b
                den_d = x + d
                str_fd = "\\frac{%s}{%s}" % (latex(num_d), latex(den_d))
                root_d = -d

                # 2. Phương án sai 1 (phân thức bậc 2 trên bậc 1, nghiệm của mẫu bị triệt tiêu hoàn toàn bởi tử -> lỗ hổng, không phải TCĐ)
                m = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
                n = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
                while m == n:
                    n = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])

                num_s1 = x**2 + (m+n)*x + m*n
                den_s1 = x + m
                str_fs1 = "\\frac{%s}{%s}" % (latex(num_s1), latex(den_s1))
                root_s1 = -m
                simp_s1 = x + n

                # 3. Phương án sai 2 (phân thức bậc 2 trên bậc 2, mẫu luôn vô nghiệm)
                r = random.choice([1, 2, 3, 4, 5])
                p = random.choice([1, 2, 3])
                if p == 1:
                    str_fs2 = "\\frac{x^2}{x^2 + %s}" % r
                else:
                    str_fs2 = "\\frac{%sx^2}{x^2 + %s}" % (p, r)

                # 4. Phương án sai 3 (hàm chứa căn thức trên tử, không có mẫu)
                k = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
                if k > 0:
                    str_fs3 = "\\sqrt{x^2 + %s}" % k
                else:
                    str_fs3 = "\\sqrt{x^2 - %s}" % abs(k)

                # Các đáp án
                da = '$y = %s$' % str_fd
                s = [
                    '$y = %s$' % str_fs1,
                    '$y = %s$' % str_fs2,
                    '$y = %s$' % str_fs3
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Đồ thị của hàm số nào dưới đây có tiệm cận đứng?''')

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Xét các phương án: \\\\
            + Với hàm số $y = %s$, tập xác định là $D = \\mathbb{R} \\setminus \\{%s\\}$. Ta có $\\lim\\limits_{x \\to %s^+} y = \\infty$ nên đường thẳng $x = %s$ là tiệm cận đứng của đồ thị hàm số. \\\\
            + Với hàm số $y = %s = %s$ (với $x \\neq %s$). Do đó đồ thị hàm số không có tiệm cận đứng. \\\\
            + Với hàm số $y = %s$, tập xác định $D = \\mathbb{R}$. Đồ thị hàm số không có tiệm cận đứng. \\\\
            + Với hàm số $y = %s$, đồ thị hàm số không có tiệm cận đứng.''' % (
                    str_fd, latex(root_d), latex(root_d), latex(root_d),
                    str_fs1, latex(simp_s1), latex(root_s1),
                    str_fs2,
                    str_fs3
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

