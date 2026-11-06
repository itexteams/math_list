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


def bt_dang19_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                i=randint(1,9)
                k=3*i
                rong=4*k
                cao=6*k

                x=symbols('x')
                a1=Rational(4*k,(2*k)**2)
                y1=a1*x**2
                s1 = integrate(4*k-y1, (x, 0, 2*k))

                a2=-Rational(2*k,k**2)
                y2=a2*x**2
                s2 = integrate(y2+k, (x, 0, k))
                h1=2*(s1+s2)   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Một người muốn trang trí cửa sổ bằng rèm vải phẳng  với đường viền là các đường parabol như hình vẽ. Biết kích thước khung làm rèm cửa là $%s$ cm và $%s$ cm (không tính phần khung viền bên ngoài). Tính Diện tích phần rèm.}
                                {\\definecolor{ffdxqq}{rgb}{1.,0.8431372549019608,0.}
                        \\scalebox{0.6}{
                            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                            \\clip(-0.41249605168673215,-0.18875285657178403) rectangle (5.609136934564493,6.362389778777163);
                            \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426, smooth,samples=50,domain=0.0:1.0] plot(\\x,{0-2*(\\x)^(2)+2}) -- (1.,0.) -- (0.,0.) -- cycle;
                            \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426, smooth,samples=50,domain=3.0:4.0] plot(\\x,{0-2*((\\x)-4)^(2)+2}) -- (4.,0.) -- (3.,0.) -- cycle;
                            \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426] {[smooth,samples=50,domain=0.0:2.0] plot(\\x,{6.0})} -- (2.,6.) {[smooth,samples=50,domain=2.0:0.0] -- plot(\\x,{(\\x)^(2)+2})} -- (0.,6.) -- cycle;
                            \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426] {[smooth,samples=50,domain=2.0:4.0] plot(\\x,{6.0})} -- (4.,2.) {[smooth,samples=50,domain=4.0:2.0] -- plot(\\x,{((\\x)-4)^(2)+2})} -- (2.,6.) -- cycle;
                            \\draw [line width=1.pt] (0.,0.)-- (-0.20398301110517095,0.);
                            \\draw [line width=1.pt] (-0.20398301110517095,0.)-- (-0.2,6.2);
                            \\draw [line width=1.pt] (-0.2,6.2)-- (4.2,6.2);
                            \\draw [line width=1.pt] (4.2,6.2)-- (4.2,0.);
                            \\draw [line width=1.pt] (4.2,0.)-- (4.,0.);
                            \\draw [line width=1.pt] (0.,6.)-- (-0.2,6.2);
                            \\draw [line width=1.pt] (4.,6.)-- (4.2,6.2);
                            \\draw [line width=1.pt] (0.,6.)-- (4.,6.);
                            \\draw [line width=1.pt] (4.,6.)-- (4.,0.);
                            \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                            \\draw [line width=1.pt] (0.,0.)-- (0.,6.);
                            \\draw [->,line width=1.pt] (4.4,1.) -- (4.4,2.);
                            \\draw [->,line width=1.pt] (4.4,1.) -- (4.4,0.);
                            \\draw (4.4,1.3751477349494872) node[anchor=north west] {$%s$cm};
                            \\draw (0,0.6) node[anchor=north west] {$%s$cm};
                    \\end{tikzpicture} } }'''
                                %(latex(rong),latex(cao),latex(2*k),latex(k)
                                ))

                # Nội dung lời giải
                loigiai = ('''\\definecolor{ffdxqq}{rgb}{1.,0.8431372549019608,0.}
            \\begin{center}
            \\scalebox{0.6}{ 
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\clip(-1.2006732728306662,-0.6240508286144383) rectangle (5.681169337685463,7.083612895163587);
                \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426, smooth,samples=50,domain=0.0:1.0] plot(\\x,{0-2*(\\x)^(2)+2}) -- (1.,0.) -- (0.,0.) -- cycle;
                \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426, smooth,samples=50,domain=3.0:4.0] plot(\\x,{0-2*((\\x)-4)^(2)+2}) -- (4.,0.) -- (3.,0.) -- cycle;
                \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426] {[smooth,samples=50,domain=0.0:2.0] plot(\\x,{6.0})} -- (2.,6.) {[smooth,samples=50,domain=2.0:0.0] -- plot(\\x,{(\\x)^(2)+2})} -- (0.,6.) -- cycle;
                \\draw[line width=0.8pt,color=ffdxqq,fill=ffdxqq,fill opacity=0.5699999928474426] {[smooth,samples=50,domain=2.0:4.0] plot(\\x,{6.0})} -- (4.,2.) {[smooth,samples=50,domain=4.0:2.0] -- plot(\\x,{((\\x)-4)^(2)+2})} -- (2.,6.) -- cycle;
                \\draw [line width=1.pt] (0.,0.)-- (-0.20398301110517095,0.);
                \\draw [line width=1.pt] (-0.20398301110517095,0.)-- (-0.2,6.2);
                \\draw [line width=1.pt] (-0.2,6.2)-- (4.2,6.2);
                \\draw [line width=1.pt] (4.2,6.2)-- (4.2,0.);
                \\draw [line width=1.pt] (4.2,0.)-- (4.,0.);
                \\draw [line width=1.pt] (0.,6.)-- (-0.2,6.2);
                \\draw [line width=1.pt] (4.,6.)-- (4.2,6.2);
                \\draw [line width=1.pt] (0.,6.)-- (4.,6.);
                \\draw [line width=1.pt] (4.,6.)-- (4.,0.);
                \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                \\draw [line width=1.pt] (0.,0.)-- (0.,6.);
                \\draw [->,line width=1.pt] (4.4,1.) -- (4.4,2.);
                \\draw [->,line width=1.pt] (4.4,1.) -- (4.4,0.);
                \\draw (4.580074520002882,1.4042817302745159) node[anchor=north west] {$60$ cm};
                \\draw [->,line width=1.pt] (-1.,2.) -- (5.,2.);
                \\draw [->,line width=1.pt] (0.,6.) -- (0.,7.);
                \\draw (4.565586430296532,2.5) node[anchor=north west] {$x$};
                \\draw (-0.5,7) node[anchor=north west] {$y$};
                \\draw (0,2.53) node[anchor=north west] {$O$};
                \\draw (1.465135233137687,0) node[anchor=north west] {$%s$ cm};
                \\draw (4.3,4.591661465671444) node[anchor=north west] {$%s$ cm};
                \\draw (0,0.6) node[anchor=north west] {$%s$cm};
            \\end{tikzpicture} }
            \\end{center}
            Gắn hệ trục tọa độ $(Oxy)$ như hình vẽ. \\\\
            Gọi pararabol phía trên là $y_1=ax^2$, parabol đi qua điểm $(%s;%s)$ nên $%s=%s^2 a \\Leftrightarrow a=%s$. \\\\
            Suy ra $y_1=%s$ nên diện tích một nửa rèm bên trên là \\\\
            $S_1=\\int \\limits_{0}^{%s} \\left( %s-%s \\right) \\text{d} x=%s$. \\\\
            Gọi pararabol phía dưới là $y_2=ax^2$, parabol đi qua điểm $(%s;-%s)$ nên $-%s=%s^2 a \\Leftrightarrow a=%s$. \\\\
            Suy ra $y_2=%s$ nên diện tích một nửa rèm bên dưới là \\\\
            $S_2=\\int \\limits_{0}^{%s} \\left( %s+%s \\right) \\text{d} x=%s$. \\\\
            Vậy diện tích rèm cửa là $S=2(S_1+S_2)=2 \\left(%s+%s\\right)=%s$.'''
                        %(latex(4*k),latex(4*k),latex(k),
                            latex(2*k),latex(4*k),latex(4*k),latex(2*k),latex(a1),
                            latex(y1),
                            latex(2*k),latex(4*k),latex(y1),latex(s1),
                            latex(k),latex(2*k),latex(2*k),latex(k),latex(a2),
                            latex(y2),
                            latex(k),latex(y2),latex(k),latex(s2),
                            latex(s1),latex(s2),latex(2*(s1+s2))
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 
