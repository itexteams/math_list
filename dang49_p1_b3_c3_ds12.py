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


def bt_dang49_p1_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # 1. Thông số cố định từ hàm số y = 4 - x^2
                # Ta chọn diện tích S = k/3 với k nguyên để bài toán đẹp
                # Diện tích tối đa từ -2 đến 2 là 32/3, nên chọn k trong khoảng (0, 32)
                # Để đảm bảo phương trình m^3 - 12m + (16-k) = 0 có nghiệm trong (-2, 2)
                # và m^3 - 12m - (16+k) = 0 vô nghiệm như trong mẫu.
                list_k = [17, 19, 20, 23, 25, 26, 29]
                k = random.choice(list_k)
                S_tex = r'\frac{%s}{3}' % k

                # Các giá trị hằng số trong lời giải
                # Phương trình: m^3 - 12m + (16 - k) = 0  (1)
                # Phương trình: m^3 - 12m - (16 + k) = 0  (2)
                c1 = 16 - k
                c2 = - (16 + k)

                # Đáp án đúng luôn là 1 giá trị của m dựa trên tính đơn điệu
                da_dung = '1'

                # Các đáp án nhiễu
                s = ['0', '2', '3', 'Vô số']
                random.shuffle(s)
                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = (r'''Đặt $S$ là diện tích của hình phẳng giới hạn bởi đồ thị của hàm số $y = 4 - x^2$, trục hoành và đường thẳng $x = -2$, $x = m$, $(-2 < m < 2)$. Số giá trị của tham số $m$ để $S = %s$ là'''
                                 % (S_tex))

                # Các đáp án trắc nghiệm
                da_d = r'\True ' + da_dung
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                list_ans = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_ans)

                # Nội dung lời giải
                loigiai = (r'''Ta có $S = \int\limits_{-2}^{m} \left| 4 - x^2 \right| \text{d}x = %s$. \\
                           Phương trình $4 - x^2 = 0 \Leftrightarrow x = \pm 2$. \\
                           Vì $-2 < m < 2$ nên trên $(-2; m)$ thì $4 - x^2 = 0$ vô nghiệm. \\
                           $\int\limits_{-2}^{m} \left| 4 - x^2 \right| \text{d}x = %s \Leftrightarrow \left| \int\limits_{-2}^{m} (4 - x^2) \text{d}x \right| = %s \Leftrightarrow \left| \left( 4x - \frac{x^3}{3} \right) \bigg|_{-2}^{m} \right| = %s$ \\
                           $\Leftrightarrow \left| \left( 4m - \frac{m^3}{3} \right) - \left( -8 + \frac{8}{3} \right) \right| = %s \Leftrightarrow \left| 4m - \frac{m^3}{3} + \frac{16}{3} \right| = %s$ \\
                           $\Leftrightarrow \left[ \begin{aligned} & 4m - \frac{m^3}{3} + \frac{16}{3} = \frac{%s}{3} \\ & 4m - \frac{m^3}{3} + \frac{16}{3} = -\frac{%s}{3} \end{aligned} \right. \Leftrightarrow \left[ \begin{aligned} & m^3 - 12m + %s = 0 \\ & m^3 - 12m + %s = 0 \end{aligned} \right. \quad (1)$ \\
                           Xét hàm số $f(m) = m^3 - 12m$, với $m \in (-2; 2)$ có $f'(m) = 3m^2 - 12 < 0, \forall m \in (-2; 2)$. \\
                           Do đó $f(m)$ nghịch biến trên $(-2; 2) \Rightarrow f(2) < f(m) < f(-2) \Leftrightarrow -16 < f(m) < 16$. \\
                           Khi đó: \\
                           $m^3 - 12m = -%s \Leftrightarrow f(m) = -%s$ (Có 1 nghiệm vì $-16 < -%s < 16$). \\
                           $m^3 - 12m = %s \Leftrightarrow f(m) = %s$ (Vô nghiệm vì %s > 16). \\
                           Vậy chỉ có 1 giá trị của $m$ thỏa mãn bài toán.'''
                           % (S_tex, S_tex, S_tex, S_tex, S_tex, S_tex, k, k, c1, -c2, c1, c1, c1, -c2, -c2, -c2))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\choice \n'
                       '{' + str(list_ans[0]) + '}\n'
                       '{' + str(list_ans[1]) + '}\n'
                       '{' + str(list_ans[2]) + '}\n'
                       '{' + str(list_ans[3]) + '}\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n').replace('--', '').replace('+ -', '-')
            return content

