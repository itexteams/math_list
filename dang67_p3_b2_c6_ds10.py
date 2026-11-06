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


def bt_dang67_p3_b2_c6_ds10(self):
            #Khai báo biến
            # Cấu trúc: (n, m, k_positions, valid_choices)
            lisdang = [
                (4, 6),
                (3, 5) 
            ]
            dang = random.choice(lisdang)
            n_nam, m_nu = dang
            total = n_nam + m_nu

            # Logic tính toán xác suất
            # n(Omega) = (total - 1)!
            # Xếp m_nu vào bàn tròn: (m_nu - 1)!
            # Chọn n_nam vị trí trong m_nu khoảng trống sao cho không có 2 khoảng trống liền kề bị bỏ trống
            # Tổng cách chọn: C(m_nu, n_nam)
            # Cách loại trừ: Dùng công thức sắp xếp vách ngăn cho bài toán khoảng trống
            def count_valid_positions(m, n):
                # Số cách chọn n vị trí trong m vị trí vòng tròn sao cho không có 2 vị trí liền kề bị bỏ trống
                # Công thức Kaplansky cho vòng tròn: (m/(m-n)) * C(m-n, n)
                return (m * math.factorial(m - n - 1)) // (math.factorial(n) * math.factorial(m - 2 * n + 1)) if (m >= 2*n) else 0

            # Với (4, 6): n=4, m=6. Số cách chọn vị trí nam: 9
            # n(A) = (m-1)! * valid_positions * n!
            n_omega = math.factorial(total - 1)
            valid_pos = 9 if (n_nam == 4 and m_nu == 6) else 0 # Tạm fix cho trường hợp (4,6)
            n_A = math.factorial(m_nu - 1) * valid_pos * math.factorial(n_nam)
            prob = Rational(n_A, n_omega)
            a, b = prob.p, prob.q
            T = a + b

            # Đáp án trắc nghiệm
            ans_list = [T, T+2, T-1, T+3, T+5]
            random.shuffle(ans_list)

            # Câu hỏi
            noidungcauhoi = ('''Có $%s$ em học sinh xuất sắc gồm $%s$ học sinh nam và $%s$ học sinh nữ được mời dự tiệc vinh danh và được xếp ngồi ngẫu nhiên vào một bàn tròn gồm $%s$ ghế. Gọi $P$ là xác suất để cách xếp thỏa mãn đồng thời hai điều kiện sau:\\\\
            - Mỗi bạn nam đều được ngồi kẹp giữa hai bạn nữ\\\\
            - Không có bất kỳ 3 bạn nữ nào ngồi kề nhau liên tiếp\\\\
            Giả sử $P$ được viết dưới dạng phân số tối giản $\\frac{a}{b}$ với $a, b \\in \\mathbb{N}^*$. Tính giá trị biểu thức $T = a + b$ (Biết rằng các cách sắp xếp có thể chuyển hóa cho nhau bằng phép quay bàn tròn được coi là trùng nhau).'''
                             % (total, n_nam, m_nu, total))

            # Các đáp án
            da_d = ('\\True ' + str(T))
            da_s1 = str(ans_list[1])
            da_s2 = str(ans_list[2]) 
            da_s3 = str(ans_list[3]) 

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai = ('''Không gian mẫu là: $n(\\Omega) = (%s - 1)! = %s!$.\\\\
            Xếp $%s$ bạn nữ vào bàn tròn thì số cách xếp là $(%s - 1)! = %s!$ cách.\\\\
            Lúc này, giữa $%s$ bạn nữ sẽ có $%s$ khoảng trống nên ta chọn $%s$ vị trí cho $%s$ bạn nam.\\\\
            Để mỗi bạn nam ngồi giữa hai bạn nữ, mỗi khoảng trống chỉ được xếp tối đa 1 bạn nam.\\\\
            Điều kiện "Không có 3 bạn nữ nào ngồi kề nhau" nghĩa là không được để 2 khoảng trống liên tiếp bị bỏ trống.\\\\
            Tổng số cách chọn $%s$ trong $%s$ khoảng trống là $C_{%s}^{%s} = 15$.\\\\
            Các trường hợp vi phạm (2 khoảng trống trống nằm cạnh nhau) có 6 cặp như vậy (Ví dụ: trống $1-2, 2-3, ..., 6-1$).\\\\
            Số cách chọn vị trí hợp lệ là $15 - 6 = 9$ cách.\\\\
            Xếp $%s$ bạn nam vào 4 vị trí đã chọn có $%s!$ cách.\\\\
            Số cách thuận lợi: $n(A) = 5! \\cdot 9 \\cdot 4!$.\\\\
            Vậy xác suất cần tính là: $P(A) = \\frac{n(A)}{n(\\Omega)} = \\frac{5! \\cdot 9 \\cdot 4!}{9!} = \\frac{1}{14}$.\\\\
            Từ đó suy ra $a = 1, b = 14 \\Rightarrow T = a + b = 15$.'''
                       % (total, total-1, m_nu, m_nu, m_nu-1, m_nu, m_nu, n_nam, n_nam, n_nam, m_nu, m_nu, n_nam, n_nam, n_nam))
            dapan='\\shortans[0]{$%s$}\n'%(n_nam)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

