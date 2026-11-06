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


def bt_dang67_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tham số k cho bán kính R = k*sqrt(2)
                # Lấy các số chẵn để quá trình chia 2 ra số nguyên đẹp
                k = random.choice([20, 30, 40, 50, 60, 80])

                c = k
                a = 2 * k
                half_c = c // 2
                two_c = 2 * c
                c2 = c**2

                # Tính toán diện tích chính xác và làm tròn đến hàng đơn vị
                exact_area = 4 * c**2 / 3
                kq = round(exact_area)

                # Các đáp án trắc nghiệm
                da = str(kq)

                # Tạo các phương án nhiễu
                s_set = set()
                s_set.add(str(round(2 * c**2 / 3)))
                s_set.add(str(round(8 * c**2 / 3)))
                s_set.add(str(round(0.5 * a**2 - (2/3) * c * half_c)))
                s_set.add(str(kq + random.choice([12, -15, 25, -28])))

                # Đảm bảo có đủ 3 đáp án sai khác với đáp án đúng
                s_set.discard(da)
                s = list(s_set)[:3]
                while len(s) < 3:
                    s.append(str(kq + random.randint(30, 100)))

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]
                hinhve=r'''\begin{center} \begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
            	\fill[cyan!20] (-2,2) -- (0,2) 
            	-- plot[variable=\t, domain=2:-2, samples=100] ({\t*\t/4 - 1}, {\t}) 
            	-- (0,-2) -- (-2,-2) -- cycle;
            	\draw[dashed, thin] (0,0) circle ({sqrt(8)});
            	\draw[->, thin] (-3.2, 0) -- (3.2, 0) node[above] {$x$};
            	\draw[->, thin] (0, -3.2) -- (0, 3.2) node[right] {$y$};
            	\draw[red, thick] (-2,-2) rectangle (2,2);
            	\draw[blue, thick, variable=\t, domain=-2.6:2.6, samples=100] plot ({\t*\t/4 - 1}, {\t});
            	\coordinate (M) at (-0.75, 1);
            	\coordinate (H) at (-2, 1); 
            	\draw[red, thick, dashed] (M) -- (H);
            	\draw[red, thick, dashed] (M) -- (0,0);
            	\fill (-2,2) circle (1.2pt) node[above left] {$A$};
            	\fill (-2,-2) circle (1.2pt) node[below left] {$B$};
            	\fill (2,-2) circle (1.2pt) node[below right] {$C$};
            	\fill (2,2) circle (1.2pt) node[above right] {$D$};
            	\fill (0,2) circle (1.2pt) node[above left] {$E$};
            	\fill (0,-2) circle (1.2pt) node[below left] {$F$};
            	\fill (-1,0) circle (1.2pt) node[above left] {$K$};
            	\fill (M) circle (1.2pt) node[above] {$M$};
            	\fill (H) circle (1.2pt); 
            	\fill (0,0) circle (1.2pt) node[above right] {$I \equiv O$};
            \end{tikzpicture} \end{center}'''
                # Câu hỏi
                noidungcauhoi = ('''Cho hình vuông $ABCD$ nội tiếp đường tròn tâm $I$, bán kính $R=%s\\sqrt{2}$ (cm). Gọi $(H)$ là miền chứa tất cả các điểm $M$ nằm bên trong hình vuông sao cho độ dài $MI \\ge d(M,AB)$. Khi đó diện tích hình phẳng $(H)$ bằng bao nhiêu centimet vuông? (Kết quả làm tròn đến hàng đơn vị).''' % (c))

                # Các đáp án
                da_d = ('\\True $%s$' % da)
                da_s1 = ('$%s$' % das1)
                da_s2 = ('$%s$' % das2)
                da_s3 = ('$%s$' % das3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết
                loigiai = ( r'''%s'''
                           '''Bán kính đường tròn $R=%s\\sqrt{2}$ nên suy ra đường chéo của hình vuông bằng $%s\\sqrt{2}$ nên cạnh hình vuông bằng $%s$ cm. \\\\
            Các điểm $M$ thỏa mãn $MI = d(M,AB)$ nằm trên một đường cong có phương trình $y = f(x)$ và đây chính là một parabol có tiêu điểm $I$ và đường chuẩn $AB$. Khi đó hình phẳng $(H)$ chính là miền được tô màu như hình vẽ. \\\\
            Gọi $M(x;y) \\Rightarrow \\begin{cases} MI = \\sqrt{x^2 + y^2} \\\\ d(M,AB) = |x + %s| \\end{cases} \\Rightarrow \\sqrt{x^2 + y^2} = |x + %s| \\Leftrightarrow y = \\pm\\sqrt{%sx + %s}$. \\\\
            Giao điểm của parabol với hai cạnh $AD$ và $BC$ là: $\\begin{cases} y = \\pm\\sqrt{%sx + %s} \\\\ y = \\pm %s \\end{cases}$ nên suy ra $E(0;%s)$; $F(0;-%s)$. \\\\
            Diện tích hình phẳng $(H)$ cần tính có thể dùng tích phân hoặc công thức tính nhanh diện tích cổng parabol: 
            $$S_{(H)} = 2 \\left( \\int\\limits_{-%s}^{-%s} |%s|dx + \\int\\limits_{-%s}^{0} \\left| %s - \\sqrt{%sx + %s} \\right|dx \\right) = %s \\text{ (cm}^2\\text{)}$$
            Khi thành thạo rồi thì ta có thể tư duy nhanh về dữ kiện đề bài cho. Ta thấy hình phẳng $(H)$ nằm bên trong hình vuông, đồng thời thỏa mãn điều kiện $MI \\ge d(M,AB)$ thì đây là miền hình phẳng nằm bên trong hình vuông, giới hạn bởi một đường parabol có tiêu điểm là $I$, đường chuẩn $AB$ và miền cần tính chứa đường chuẩn $AB$, bao gồm cả đường parabol. \\\\
            Tính diện tích dựa trên công thức tính nhanh: \\\\
            $$S_{(H)} = \\frac{1}{2} S_{ABCD} - \\frac{4}{3} \\cdot EI \\cdot KI = \\frac{1}{2} \\cdot %s^2 - \\frac{4}{3} \\cdot %s \\cdot %s = %s \\text{ (cm}^2\\text{)}.$$''' % 
                    (hinhve, c, 2*c, a, 
                     c, c, two_c, c2, 
                     two_c, c2, c, c, c,
                     c, half_c, c, half_c, c, two_c, c2, kq,
                     a, c, half_c, kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

