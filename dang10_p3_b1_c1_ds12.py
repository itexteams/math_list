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


def bt_dang10_p3_b1_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Chọn ngẫu nhiên nghiệm cực tiểu x1 và nghiệm cực đại x2 để tạo số nguyên đẹp
                # x1 là thời điểm doanh thu bắt đầu tăng trở lại (tính bằng nghìn sản phẩm)
                x1 = randint(1, 3)
                x2 = x1 + randint(3, 5)

                # Để đồ thị có hệ số bậc ba là âm (đảm bảo doanh thu giảm rồi tăng rồi giảm)
                # R'(x) = -6*(x - x1)*(x - x2) = -6x^2 + 6*(x1 + x2)*x - 6*x1*x2
                # R(x) = -2x^3 + 3*(x1 + x2)*x^2 - 6*x1*x2*x + D
                coeff_a = -2
                coeff_b = 3 * (x1 + x2)
                coeff_c = -6 * x1 * x2
                D_val = randint(100, 300)

                # Kết quả đúng là x1 nghìn sản phẩm -> làm tròn đến hàng đơn vị của sản phẩm
                kq_num = x1 * 1000
                kq = str(kq_num)

                # Các đáp án trắc nghiệm sai lệch quanh đáp án đúng
                du = ['$%s$ sản phẩm' % (kq)]
                da = random.choice(du)

                s = [
                    '$%s$ sản phẩm' % (str((x1 + 1) * 1000)),
                    '$%s$ sản phẩm' % (str(x2 * 1000)),
                    '$%s$ sản phẩm' % (str(abs(x1 - 1) * 1000) if x1 > 1 else "500"),
                    '$%s$ sản phẩm' % (str((x2 - 1) * 1000)),
                    '$%s$ sản phẩm' % (str((x1 + 2) * 1000))
                ]
                s = [item for item in s if item != da]
                s = list(set(s))

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Biểu diễn phương trình R(x)
                sign_b = '+' if coeff_b >= 0 else ''
                sign_c = '+' if coeff_c >= 0 else ''

                noidungcauhoi = ('''Một công ty sản xuất sản phẩm và doanh thu (đơn vị: triệu đồng) từ việc bán sản phẩm được mô tả bởi hàm số $R(x) = %sx^3 %s %sx^2 %s %sx + %s$. Trong đó, $x$ là số lượng sản phẩm được bán ra (tính bằng ngàn sản phẩm). Hỏi số lượng sản phẩm tối thiểu phải bán ra để doanh thu bắt đầu tăng là bao nhiêu sản phẩm? (Kết quả làm tròn đến hàng đơn vị).'''
                                 % (latex(coeff_a), sign_b, latex(coeff_b), sign_c, latex(coeff_c), latex(D_val)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Đạo hàm của R(x)
                der_a = 3 * coeff_a
                der_b = 2 * coeff_b
                der_c = coeff_c
                sign_der_b = '+' if der_b >= 0 else ''
                sign_der_c = '+' if der_c >= 0 else ''

                # Nội dung lời giải chi tiết, lập bảng biến thiên bằng TikZ
                loigiai = ('''Xét hàm số doanh thu $R(x) = %sx^3 %s %sx^2 %s %sx + %s$ với $x \\ge 0$.\\\\
                           Ta có đạo hàm của hàm số là:\\\\
                           $R'(x) = %sx^2 %s %sx %s %s$.\\\\
                           Cho $R'(x) = 0 \\Leftrightarrow %sx^2 %s %sx %s %s = 0 \\Leftrightarrow \\left[\\begin{aligned} & x = %s \\\\ & x = %s \\end{aligned}\\right.$.\\\\
                           Ta lập bảng biến thiên của hàm số $R(x)$ trên nửa khoảng $[0; +\\infty)$ như sau:\\\\
                           \\begin{center}
                           \\begin{tikzpicture}[scale=1]
                           \\draw[line width=1pt] (0,3) -- (10,3);
                           \\draw[line width=1pt] (0,2) -- (10,2);
                           \\draw[line width=1pt] (2,0) -- (2,4);
                           \\node at (1,3.5) {$x$};
                           \\node at (2.3,3.5) {$0$};
                           \\node at (4.5,3.5) {$%s$};
                           \\node at (7.0,3.5) {$%s$};
                           \\node at (9.5,3.5) {$+\\infty$};
                           \\node at (1,2.5) {$R'(x)$};
                           \\node at (3.4,2.5) {$-$};
                           \\node at (4.5,2.5) {$0$};
                           \\node at (5.7,2.5) {$+$};
                           \\node at (7.0,2.5) {$0$};
                           \\node at (8.2,2.5) {$-$};
                           \\node at (1,1) {$R(x)$};
                           \\draw[->,line width=1pt] (2.5,1.7) -- (4.2,0.3);
                           \\draw[->,line width=1pt] (4.8,0.3) -- (6.7,1.7);
                           \\draw[->,line width=1pt] (7.3,1.7) -- (9.2,0.3);
                           \\end{tikzpicture}
                           \\end{center}
                           Dựa vào bảng biến thiên, ta thấy trên khoảng $[0; %s)$, đạo hàm $R'(x) < 0$ nên hàm số nghịch biến (doanh thu giảm).\\\\
                           Trên khoảng $(%s; %s)$, đạo hàm $R'(x) > 0$ nên hàm số đồng biến (doanh thu bắt đầu tăng).\\\\
                           Như vậy, doanh thu bắt đầu tăng khi số lượng sản phẩm bán ra $x$ vượt qua giá trị cực tiểu $x = %s$ (ngàn sản phẩm).\\\\
                           Đổi ra đơn vị sản phẩm: $%s \\cdot 1000 = %s$ sản phẩm.\\\\
                           Vậy số lượng sản phẩm tối thiểu phải bán ra để doanh thu bắt đầu tăng là $%s$ sản phẩm.'''
                           % (latex(coeff_a), sign_b, latex(coeff_b), sign_c, latex(coeff_c), latex(D_val),
                              latex(der_a), sign_der_b, latex(der_b), sign_der_c, latex(der_c),
                              latex(der_a), sign_der_b, latex(der_b), sign_der_c, latex(der_c), latex(x1), latex(x2),
                              latex(x1), latex(x2),
                              latex(x1), latex(x1), latex(x2), latex(x1), latex(x1), latex(kq), latex(kq)))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content  

