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


def bt_dang20_p3_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Giả định các biến đã được khởi tạo như trong code của bạn
            # Để code chạy được, tôi tạo các bộ số ngẫu nhiên mẫu:
            setups = [
                {'A1': 1, 'B1': -sqrt(3), 'alpha_deg': 60},
                {'A1': sqrt(3), 'B1': -1, 'alpha_deg': 30},
                {'A1': 1, 'B1': -1, 'alpha_deg': 45}
            ]
            choice = random.choice(setups)
            A1, B1, alpha_deg = choice['A1'], choice['B1'], choice['alpha_deg']
            C1, C2 = random.randint(1, 10), random.randint(1, 10)

            # Tính toán logic
            m = symbols('m', real=True)
            cos_alpha = cos(alpha_deg * pi / 180)
            mau_so_truoc = sp.simplify(sqrt(A1**2 + B1**2))
            # Giải phương trình tìm m
            phuong_trinh = sp.Eq(cos_alpha, Abs(A1*m + B1) / (mau_so_truoc * sqrt(m**2 + 1)))
            solutions = solve(phuong_trinh, m)
            m_val = solutions[0] if solutions else 0

            # --- Xử lý hiển thị để không bị lỗi thiếu tử số và lỗi định dạng ---
            # Tạo chuỗi b1_hien_thi bao gồm cả dấu và giá trị tuyệt đối (VD: - \sqrt{3})
            b1_hien_thi = ('+ ' + latex(abs(B1)) if B1 > 0 else '- ' + latex(abs(B1)))
            # Nếu A1 = 1 thì không hiện số 1 trước m (hiện "m" thay vì "1m")
            a1_rut_gon = latex(A1) if A1 != 1 else ''
            # Hệ số sau khi chuyển vế: k = cos(alpha) * sqrt(A1^2 + B1^2)
            he_so_k = sp.simplify(cos_alpha * mau_so_truoc)

            # Nội dung câu hỏi
            noidungcauhoi = (r'Giá trị của $m$ để góc hợp bởi hai đường thẳng $\Delta_1 : %s x %s %s + %s = 0$ và $\Delta_2 : mx + y + %s = 0$ một góc bằng $%s^\circ$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'
                            % (latex(A1), '+' if B1 > 0 else '-', latex(abs(B1)) if abs(B1) != 1 else 'y', C1, C2, alpha_deg))
            noidungcauhoi = noidungcauhoi.replace('1 x', 'x').replace('1 y', 'y').replace('+ -', '-')

            # Đáp án trắc nghiệm
            da_d = '\\True $m = ' + latex(m_val) + '$'
            list_1 = [da_d, '$m = 0$', '$m = \\sqrt{3}$', '$m = 1$']
            random.shuffle(list_1)

            # --- BẢN SỬA LỖI LOIGIAI (KHỚP 20 BIẾN %s) ---
            h1=m_val
            number = Decimal(float(h1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            kqz=str(kq1).replace('.',',')
            loigiai = (r'''Ta có $\cos(\Delta_1;\Delta_2) = \frac{|m \cdot %s + (%s) \cdot 1|}{\sqrt{(%s)^2 + (%s)^2} \cdot \sqrt{m^2 + 1}} = \frac{|%s m %s|}{%s \sqrt{m^2+1}}$. \\
            Theo giả thiết, góc hợp bởi hai đường thẳng $\Delta_1, \Delta_2$ bằng $%s^\circ$ nên: \\
            $\cos %s^\circ = \frac{|%s m %s|}{%s \sqrt{m^2+1}} \Leftrightarrow %s \sqrt{m^2+1} = |%s m %s|$ \\
            $\Leftrightarrow %s(m^2+1) = (%s m %s)^2 \Leftrightarrow m = %s$. \\
            Vậy $m = %s$ là giá trị cần tìm.'''
                % (latex(A1), latex(B1), latex(A1), latex(B1),              # Tử & mẫu 1 (4 biến)
                   a1_rut_gon, b1_hien_thi, latex(mau_so_truoc),            # Tử & mẫu 2 (3 biến) - ĐÃ SỬA B1_HIEN_THI
                   alpha_deg,                                               # Dòng giả thiết (1 biến)
                   alpha_deg, a1_rut_gon, b1_hien_thi, latex(mau_so_truoc), # Phân số cos (4 biến)
                   latex(he_so_k), a1_rut_gon, b1_hien_thi,                 # Sau dấu <=> 1 (3 biến)
                   latex(he_so_k**2), a1_rut_gon, b1_hien_thi,              # Sau dấu <=> 2 (3 biến)
                   latex(m_val), latex(m_val))                              # Kết luận (2 biến)
            )

            # Làm sạch dấu
            loigiai = loigiai.replace('+ -', '-').replace('| m', '|m').replace('(1) \\cdot 1', '1')
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kqz)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 


