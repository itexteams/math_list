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


def bt_dang7_p2_b3_c3_ds12(self):
            # Khai báo biến
            k=randint(1,9)
            a=4*k
            b=2*k 
            r=b
            v1=b**2*a-Rational(b**2*a**3,3*a**2)
            v2=Rational(4*r**3,6)

            x=symbols('x')
            f=sqrt(b**2-Rational(b**2,a**2)*x**2)

            s1 = integrate(f, (x, -a, 0))
            s2=Rational(r**2,2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một quả trứng khủng long đồ chơi là một khối tròn xoay được tạo thành từ hai mảnh ghép lại. Biết mảnh trên được tạo thành khi xoay một phần tư đường elip với trục lớn là $%s$ và trục nhỏ là $%s$ quanh trục $Ox$ và mảnh dưới được tạo thành khi xoay một phần tư đường tròn bán kính $%s$ quanh trục Ox như hình sau (bỏ qua độ dày của vỏ trứng).
            \\begin{center}
            \\scalebox{0.6}{ 
            \\begin{tikzpicture}[
                line join=round,
                line cap=round,
                >=stealth,
                thick
                ]
                \\definecolor{orange}{rgb}{1,0.5,0} 
                \\definecolor{ffqqqq}{rgb}{1,0,0} 
                \\clip (-3.2,-2.3) rectangle (3.2,4.2);
                \\draw[line width=0.8pt, color=ffqqqq, fill=ffqqqq, fill opacity=1.0]
                plot[smooth, samples=50, domain=-2:2] (\\x, {0 - sqrt(4 - \\x*\\x)}) 
                -- (2,0)
                plot[smooth, samples=50, domain=2:-2] (\\x, {0 - sqrt(1 - \\x*\\x/4)}) 
                -- (-2,0)
                -- cycle;
                \\draw[line width=0.8pt, color=orange, fill=orange, fill opacity=1.0]
                plot[smooth, samples=50, domain=-2:2] (\\x, {sqrt(16 - 4*\\x*\\x)}) 
                -- (2,0)
                plot[smooth, samples=50, domain=2:-2] (\\x, {0 - sqrt(1 - \\x*\\x/4)}) 
                -- (-2,0)
                -- cycle;
            \\end{tikzpicture}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\draw[->] (-5,0) -- (5,0) node[below] {$x$}; 
                \\draw[->] (0,-3) -- (0,3) node[left] {$y$}; 
                \\draw[thick] plot[domain=90:270, samples=100] ({4*cos(\\x)}, {2*sin(\\x)});
                \\draw[dashed] plot[domain=-90:90, samples=100] ({4*cos(\\x)}, {2*sin(\\x)});
                \\draw[thick] plot[domain=-90:90, samples=100] ({2*cos(\\x)}, {2*sin(\\x)});
                \\draw[thick] plot[domain=-90:90, samples=100] ({cos(\\x)}, {2*sin(\\x)});
                \\draw[dashed] plot[domain=90:270, samples=100] ({cos(\\x)}, {2*sin(\\x)});
                \\node[below left] at (0,0) {$O$};
                \\node[below left] at (-4,0) {$-%s$};
                \\node[below right] at (4,0) {$%s$};
                \\node[above left] at (0,2) {$%s$};
                \\node[below left] at (0,-2) {$-%s$};
            \\end{tikzpicture} } \\end{center}'''                 
                            %(latex(2*a),latex(2*b),latex(r),
                            latex(a),latex(a),latex(b),latex(b)
                                ) )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Thể tích phần trong của mảnh trên là $V_1=\\pi \\int \\limits_{%s} ^{0} \\left( %s-%s x^2 \\right) \\text{d} x$' %(latex(-a),latex(b**2),latex(Rational(b**2,a**2)))
            nb_da_1_s = 'Thể tích phần trong của mảnh trên là $V_1=\\pi \\int \\limits_{%s} ^{0} \\left( %s-%s x^2 \\right) \\text{d} x$' %(latex(-a),latex(b**2),latex(Rational(a**2,b**2)))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Phương trình elip tương ứng với mảnh trên là $\\frac{x^2}{%s}+\\frac{y^2}{%s}=1 \\Leftrightarrow y=\\pm \\sqrt{%s-%s x^2}$. \\\\
                            Nửa trên của elip được biểu diễn bởi hàm $y=\\sqrt{%s-%s x^2}$. \\\\
                                Thể tích phần trong của mảnh trên là $V_1=\\pi \\int \\limits_{%s} ^{0} \\left( %s-%s x^2 \\right) \\text{d} x$'''
                            %(latex(a**2),latex(b**2),
                            latex(b**2),latex(Rational(b**2,a**2)),
                            latex(b**2),latex(Rational(b**2,a**2)),
                            latex(-a),
                            latex(b**2),latex(Rational(b**2,a**2)),
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Thể tích phần trong của mảnh dưới là $V_2=%s \\pi$' %(latex(Rational(4*r**3,6)))  
            th_da_1_s = 'Thể tích phần trong của mảnh dưới là $V_2=%s \\pi$' %(latex(Rational(4*r**3,3)))  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Mảnh dưới là đường tròn có tâm $O(0;0)$ và bán kính $r=%s$. \\\\
                            Thể tích khối cầu tạo bởi đường tròn đó là $V_c=\\frac{4}{3} \\pi r^3=\\frac{4}{3} \\pi %s=%s \\pi$. \\\\
                                Suy ra thể tích phần trong của mảnh dưới là $V_2=\\frac{V_c}{2}=%s \\pi$.'''          
                        %(latex(r),latex(r**3),latex(Rational(4*r**3,3)),
                        latex(Rational(4*r**3,6))
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Thể tích phần trong của quả trứng là $V=%s \\pi$' %(latex(v1+v2))  
            vd_da_1_s = 'Thể tích phần trong của quả trứng là $V=%s \\pi$' %(latex(v1+v2+1))   
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có các thể tích: $V_1=\\pi \\int \\limits_{%s} ^{0} \\left( %s-%s x^2 \\right) \\text{d} x=%s \\pi$ và $V_2=%s \\pi$. \\\\
                                Vậy thể tích phần trong của quả trứng là $V=V_1+V_2=%s \\pi$'''  
                        %(latex(-a),latex(b**2),latex(Rational(b**2,a**2)),latex(v1),
                        latex(v2),
                        latex(v1+v2)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Diện tích thiết diện khi cắt bởi mặt phẳng qua trục quả trứng là $%s$' %(latex(s1+s2*pi)) 
            vdc_da_1_s = 'Diện tích thiết diện khi cắt bởi mặt phẳng qua trục quả trứng là $%s$' %(latex(s1+s2*pi+pi)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Khi cắt quả trứng bởi mặt phẳng đi qua trục thì thiết diện tạo ra gồm hai phần: \\\\
                            Phần I: Hình phẳng giới hạn bởi đồ thì hàm số $y=\\sqrt{%s-%s x^2}$ với hai đường $x=%s, x=0$.\\\\
                                Diện tích hình phẳng là $S_1=2 \\int \\limits_{%s}^{0} \\sqrt{%s-%s x^2} \\text{d} x=%s$. \\\\
                            Phần II: Hình phẳng giới hạn bởi một nữa đường tròn tâm $O$ bán kính bằng $%s$. \\\\
                                Diện tích là $S_2=\\frac{\\pi r^2}{2}=%s \\pi$. \\\\
                            Vậy diện tích thiết diện cần tìm là $S=S_1+S_2=%s$.'''
                        %(latex(b**2),latex(Rational(b**2,a**2)),latex(-a),
                        latex(-a),latex(b**2),latex(Rational(b**2,a**2)),latex(s1),
                        latex(r),latex(Rational(r**2,2)),
                        latex(2*s1+s2*pi),
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

