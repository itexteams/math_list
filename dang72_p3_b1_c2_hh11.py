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


def bt_dang72_p3_b1_c2_hh11(self):
            # Khai báo biến
            # nhưng để tính toán số học cho đáp án nhiễu, ta coi a = 1 hoặc chọn a ngẫu nhiên.
            val_a = random.randint(2, 6) 
            a = sp.symbols('a')

            # 1. Tính toán các đại lượng dựa trên đề bài
            # Đáy ABCD là hình thang vuông tại A và B, AB=BC=a, AD=2a
            # AC = sqrt(a^2 + a^2) = a*sqrt(2)
            ac = a * sqrt(2)

            # H thuộc AC sao cho CH = 3AH => AH = 1/4 AC, CH = 3/4 AC
            ah = ac / 4
            ch = (3 * ac) / 4

            # SH = a*sqrt(3)
            sh = a * sqrt(3)

            # Tính SC = sqrt(SH^2 + CH^2)
            sc_sq = sh**2 + ch**2
            sc = sqrt(sc_sq)

            # Gọi E là trung điểm AD => AE = ED = a. 
            # Vì AD // BC và AD = 2BC, E là trung điểm AD nên AE = BC = a. 
            # Tứ giác ABCE là hình vuông cạnh a => CE = a và CE // AB.
            ce = a

            # Tính HE dùng định lý cos trong tam giác AHE:
            # Góc HAE = góc DAC. Trong hình thang ABCD, AC là đường chéo hình vuông ABCE 
            # nên góc CAD = 45 độ.
            # HE^2 = AE^2 + AH^2 - 2*AE*AH*cos(45)
            cos45 = sqrt(2)/2
            he_sq = a**2 + ah**2 - 2*a*ah*cos45
            he = sqrt(he_sq)

            # Tính SE = sqrt(SH^2 + HE^2)
            se_sq = sh**2 + he_sq
            se = sqrt(se_sq)

            # Tính cos(SC, AB). Vì AB // CE nên cos(SC, AB) = cos(SC, CE)
            # Xét tam giác SCE: cos(SCE) = (SC^2 + CE^2 - SE^2) / (2 * SC * CE)
            tu_so = sc_sq + ce**2 - se_sq
            mau_so = 2 * sc * ce
            cos_phi = tu_so / mau_so

            # Đơn giản hóa kết quả
            kq_final = sp.simplify(cos_phi)

            # 2. Tạo các đáp án nhiễu
            def generate_distractors(correct_val):
                distractors = set()
                while len(distractors) < 3:
                    # Tạo biến thể bằng cách thay đổi các hệ số căn thức
                    fake = sp.sqrt(random.randint(10, 80)) / random.randint(10, 30)
                    if fake != correct_val:
                        distractors.add(f'${latex(fake)}$')
                return list(distractors)

            da_dung = f'${latex(kq_final)}$'
            nhieu = generate_distractors(kq_final)

            # 3. Nội dung câu hỏi và lời giải
            noidungcauhoi = f'''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang vuông tại $A$ và $B$. Biết $AB = BC = a$, $AD = 2a$. Hình chiếu của $S$ xuống $(ABCD)$ là điểm $H$ thuộc $AC$ sao cho $CH = 3AH$; $SH = a\\sqrt{{3}}$. Giá trị $\\cos(SC; AB)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''

            # Nội dung lời giải (Đã sửa lỗi ngoặc nhọn để tránh SyntaxError)
            loigiai = (
                '\\begin{center}'
                '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.8cm,y=0.8cm]
            	\\clip(-1.74,-3.8) rectangle (7.92,4.74);
            	\\draw [dash pattern=on 2pt off 2pt] (2.,4.)-- (2.,-1.);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,-3.);
            	\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,0.);
            	\\draw (6.,0.)-- (6.,-3.);
            	\\draw (6.,-3.)-- (3.,-3.);
            	\\draw (3.,-3.)-- (0.,0.);
            	\\draw (2.,4.)-- (0.,0.);
            	\\draw (2.,4.)-- (3.,-3.);
            	\\draw (2.,4.)-- (6.,0.);
            	\\draw (2.,4.)-- (6.,-3.);
            	\\draw [dash pattern=on 2pt off 2pt] (3.,0.)-- (6.,-3.);
            	\\draw [dash pattern=on 2pt off 2pt] (3.,-3.)-- (6.,0.);
            	\\draw (1.86,4.88) node[anchor=north west] {$S$};
            	\\draw (-0.7,0.54) node[anchor=north west] {$A$};
            	\\draw (2.56,-3) node[anchor=north west] {$B$};
            	\\draw (5.92,-3) node[anchor=north west] {$C$};
            	\\draw (6,0.52) node[anchor=north west] {$D$};
            	\\draw (2.78,0.7) node[anchor=north west] {$E$};
            	\\draw (1.68,-1) node[anchor=north west] {$H$};
            	\\draw (4.4,-3) node[anchor=north west] {$a$};
            	\\draw (1.16,-1.5) node[anchor=north west] {$a$};
            	\\draw (3.32,0.7) node[anchor=north west] {$2a$};
            	\\draw (0.8,1.6) node[anchor=north west] {$a\\sqrt{3}$};
            \\end{tikzpicture}'''
            '\\end{center}'
                f''' Ta có $AC = a\\sqrt{{2}} \\Rightarrow AH = \\frac{{a\\sqrt{{2}}}}{{4}}; CH = \\frac{{3a\\sqrt{{2}}}}{{4}}$.\\\\
            Xét tam giác vuông $SHC$ tại $H$: $SC = \\sqrt{{SH^2 + CH^2}} = \\sqrt{{3a^2 + \\frac{{9a^2}}{{8}}}} = a\\sqrt{{\\frac{{33}}{{8}}}}$.\\\\
            Gọi $E$ là trung điểm của $AD \\Rightarrow AE = a$. Vì $ABCE$ là hình vuông nên $CE \\parallel AB$ và $CE = a$.\\\\
            Do đó $(SC; AB) = (SC; CE) = \\widehat{{SCE}}$.\\\\
            Trong $\\triangle AHE$: $HE^2 = AE^2 + AH^2 - 2AE \\cdot AH \\cdot \\cos 45^\\circ = a^2 + \\frac{{2a^2}}{{16}} - 2a \\cdot \\frac{{a\\sqrt{{2}}}}{{4}} \\cdot \\frac{{\\sqrt{{2}}}}{{2}} = \\frac{{5a^2}}{{8}}$.\\\\
            Trong $\\triangle SHE$: $SE = \\sqrt{{SH^2 + HE^2}} = \\sqrt{{3a^2 + \\frac{{5a^2}}{{8}}}} = a\\sqrt{{\\frac{{29}}{{8}}}}$.\\\\
            Áp dụng định lý cosin trong $\\triangle SCE$: \\\\
            $\\cos \\widehat{{SCE}} = \\frac{{SC^2 + CE^2 - SE^2}}{{2SC \\cdot CE}} = \\frac{{\\frac{{33a^2}}{{8}} + a^2 - \\frac{{29a^2}}{{8}}}}{{2 \\cdot a\\sqrt{{\\frac{{33}}{{8}}}} \\cdot a}} = \\frac{{\\sqrt{{66}}}}{{22}} \\approx 0,4$.'''
            )
            h1=sqrt(66)/22
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            #Đáp án
            dapan='\\shortans[0]{$0,4$}\n'
            # Xuất kết quả
            list_ans = [f'\\True {da_dung}'] + nhieu
            random.shuffle(list_ans)

            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('frac','dfrac')
            return content

