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


def bt_dang12_p3_b4_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Vòng lặp tìm bộ số ngẫu nhiên thỏa mãn tính hợp lý của bài toán hình học
                while True:
                    xA = random.randint(4, 10)
                    yB = random.randint(4, 10)
                    zA = random.randint(2, 6)
                    zB = random.randint(2, 8)

                    # Bình phương khoảng cách AB
                    AB2 = xA**2 + yB**2 + (zB - zA)**2

                    # Bán kính R phải lớn hơn nửa độ dài AB để 2 mặt cầu giao nhau
                    min_R = math.ceil(math.sqrt(AB2) / 2)
                    if min_R + 3 > 12: 
                        continue # Đảm bảo R không quá lớn

                    R = random.randint(min_R + 1, min_R + 3)

                    # Tính toán chính xác bằng sympy để xuất LaTeX
                    sp_AB2 = sp.sympify(AB2)
                    sp_AB = sp.sqrt(sp_AB2)

                    sp_r2 = R**2 - sp_AB2 / 4
                    sp_r = sp.sqrt(sp_r2)

                    sp_ApBp2 = sp.sympify(xA**2 + yB**2)
                    sp_ApBp = sp.sqrt(sp_ApBp2)

                    # Tọa độ tâm I (trung điểm AB)
                    sp_Iz_x = sp.Rational(xA, 2)
                    sp_Iz_y = sp.Rational(yB, 2)
                    sp_Iz_z = sp.Rational(zA + zB, 2)
                    sp_AI = sp_AB / 2

                    # Tính chiều cao tối đa h_max
                    sp_hmax = sp_Iz_z + sp_r * (sp_ApBp / sp_AB)
                    hmax_val = float(sp_hmax)

                    if hmax_val > 0:
                        break

                # Làm tròn phần mười và chuyển sang định dạng chuỗi có dấu phẩy
                kq_float = round(hmax_val, 1)
                kq_str = str(kq_float).replace('.', ',')

                # Các đáp án trắc nghiệm
                du = ['$%s$'%(kq_str)]
                da = random.choice(du)

                # Tạo các phương án nhiễu sai khác với đáp án đúng
                s_set = set()
                while len(s_set) < 3:
                    variation = round(hmax_val + random.choice([-0.3, -0.2, -0.1, 0.1, 0.2, 0.3]), 1)
                    if variation != kq_float and variation > 0:
                        s_set.add(variation)

                s = list(s_set)
                das1 = '$%s$' % str(s[0]).replace('.', ',')
                das2 = '$%s$' % str(s[1]).replace('.', ',')
                das3 = '$%s$' % str(s[2]).replace('.', ',')

                # Câu hỏi
                noidungcauhoi = ('''Trong không gian $Oxyz$ với đơn vị trên mỗi hệ trục là $1$ mét, hai bức tường được xây vuông góc với nhau và cùng vuông góc với sàn nhà là mặt phẳng $Oxy$. Hai điểm $A(%s;0;%s)$ và $B(0;%s;%s)$ là hai điểm cố định ở hai bên bức tường. Ban đầu hai thanh $AM_1$ và $BM_2$ đều có độ dài bằng $%s$ m với hai điểm có thể di động $M_1, M_2$ thuộc mặt sàn và $1$ thợ hàn muốn kết nối hai thanh $AM_1$ và $BM_2$ bởi mối hàn $M$ để tạo thành một hệ gấp khúc $A-M-B$. Biết rằng đường gấp khúc này không bị ảnh hưởng bởi hai góc tường, khi ấy mối hàn điểm $M$ cách mặt đất $1$ khoảng cao nhất bằng bao nhiêu mét? (làm tròn đến hàng phần mười).
            \\begin{center}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0.7] 
            \\fill[brown!40] (-5,-2) -- (0,0) -- (0,4) -- (-5,2) -- cycle;
            \\fill[brown!60] (0,0) -- (5,-1.5) -- (5,2.5) -- (0,4) -- cycle;
            \\fill[green!10] (-5,-2) -- (0,0) -- (5,-1.5) -- (0,-3.5) -- cycle;
            \\draw (-5,-2) -- (0,0) -- (5,-1.5);
            \\draw (0,0) -- (0,4);
            \\draw (-5,-2) -- (-5,2) -- (0,4) -- (5,2.5) -- (5,-1.5);
            \\draw (-5,-2) -- (-5.5,-1.8) -- (-5.5,2.2) -- (-5,2);
            \\draw (-5.5,2.2) -- (-0.5,4.2) -- (0,4);
            \\draw (-0.5,4.2) -- (4.5,2.7) -- (5,2.5);
            \\draw[->] (-5,-2) -- (-6,-2.4) node[below]{$x$};
            \\draw[->] (5,-1.5) -- (6,-1.8) node[below]{$y$};
            \\draw[->] (0,4) -- (0,5) node[right]{$z$};
            \\node[below] at (0,0) {$O$};
            \\coordinate (A) at (-3, 0.5);
            \\coordinate (Ap) at (-3, -1.2);
            \\coordinate (Az) at (0, 1.7);
            \\coordinate (B) at (3, 1.2);
            \\coordinate (Bp) at (3, -0.9);
            \\coordinate (Bz) at (0, 2.1);
            \\draw[dashed] (A) -- (Ap) node[below] {$%s$};
            \\draw[dashed] (B) -- (Bp) node[below] {$%s$};
            \\draw[dashed] (A) -- (Az) node[right] {$%s$};
            \\draw[dashed] (B) -- (Bz) node[left] {$%s$};
            \\fill (A) circle (2pt) node[left] {$A$};
            \\fill (B) circle (2pt) node[right] {$B$};
            \\coordinate (M1) at (-1.5, -2.5);
            \\coordinate (M2) at (1.5, -2.2);
            \\draw[red, thick] (A) -- (M1);
            \\draw[red, thick] (B) -- (M2);
            \\fill[red] (M1) circle (2pt) node[right] {$M_1$};
            \\fill[red] (M2) circle (2pt) node[below] {$M_2$};
            \\draw[fill=gray!20] (0,-4) ellipse (1.2cm and 0.5cm);
            \\node at (0,-4) {\\footnotesize Mặt sàn};
            \\end{tikzpicture}
            \\end{center}''' % (xA, zA, yB, zB, R, xA, yB, zA, zB))

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Mặt cầu $(S_1)$ tâm $A(%s;0;%s)$, bán kính $R=%s$ là: $(S_1): (x-%s)^2 + y^2 + (z-%s)^2 = %s$\\\\
            Mặt cầu $(S_2)$ tâm $B(0;%s;%s)$, bán kính $R=%s$ là: $(S_2): x^2 + (y-%s)^2 + (z-%s)^2 = %s$\\\\
            Giao của hai mặt cầu là một đường tròn nằm trên mặt phẳng vuông góc với đường nối tâm $AB$\\\\
            Độ dài $AB = \\sqrt{%s^2 + %s^2 + %s^2} = %s$\\\\
            Gọi $I$ là trung điểm $AB$ (vì $MA=MB=%s$ nên $I$ là tâm đường tròn giao tuyến) $\\Rightarrow I\\left(%s; %s; %s\\right)$\\\\
            Bán kính đường tròn giao tuyến $r = MI = \\sqrt{MA^2 - AI^2} = \\sqrt{%s^2 - \\left(%s\\right)^2} = %s$\\\\
            Cao độ của $M$ sẽ bằng cao độ của tâm $I$ cộng với hình chiếu đứng của bán kính $MI$. Để $z_M \\max$, vectơ $IM$ phải nằm trong mặt phẳng đứng chứa $AB$.\\\\
            Gọi $\\alpha$ là góc giữa đường thẳng $AB$ và mặt phẳng $(Oxy)$\\\\
            Ta có: $\\cos\\alpha = \\frac{A'B'}{AB}$ (với $A', B'$ là hình chiếu của $A, B$ xuống sàn)\\\\
            Vậy $A'B' = \\sqrt{%s^2 + %s^2} = %s \\Rightarrow \\cos\\alpha = \\frac{%s}{%s} \\Rightarrow h_{\\max} = %s + %s \\cdot \\frac{%s}{%s} \\approx %s$ (m)''' % (
                    xA, zA, R, xA, zA, R**2,
                    yB, zB, R, yB, zB, R**2,
                    xA, yB, abs(zB-zA), sp.latex(sp_AB),
                    R, sp.latex(sp_Iz_x), sp.latex(sp_Iz_y), sp.latex(sp_Iz_z),
                    R, sp.latex(sp_AI), sp.latex(sp_r),
                    xA, yB, sp.latex(sp_ApBp), sp.latex(sp_ApBp), sp.latex(sp_AB),
                    sp.latex(sp_Iz_z), sp.latex(sp_r), sp.latex(sp_ApBp), sp.latex(sp_AB), kq_str
                ))
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{'+str(loigiai)+'}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

