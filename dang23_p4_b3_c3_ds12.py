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


def bt_dang23_p4_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                i=randint(1,9)
                d=7*i
                r=6*i
                z1=randint(20,30)
                t1=z1*10
                z2=randint(10,15)
                t2=z2*10

                x0=Rational(r,2)
                y0=Rational(d,2)

                a=2 
                b=2*y0
                c=-x0**2 
                delta=b**2-4*a*c
                x1=(-b-sqrt(delta))/(2*a)
                x2=(-b+sqrt(delta))/(2*a)

                c1=x2
                a1=Rational(c1+y0,x0**2)

                x=symbols('x')
                f=a1*x**2-c1

                x3=sqrt(c1/a1)

                s1 = integrate(f, (x, x3, x0))

                s=pi*c1**2+s1

                Ss=d*r
                Sc=Ss-s

                t=t1*s+t2*Sc
                tkq=t/1000
                while tkq>99.9:
                    i=randint(1,9)
                    d=7*i
                    r=6*i
                    z1=randint(20,30)
                    t1=z1*10
                    z2=randint(10,15)
                    t2=z2*10

                    x0=Rational(r,2)
                    y0=Rational(d,2)

                    a=2 
                    b=2*y0
                    c=-x0**2 
                    delta=b**2-4*a*c
                    x1=(-b-sqrt(delta))/(2*a)
                    x2=(-b+sqrt(delta))/(2*a)

                    c1=x2
                    a1=Rational(c1+y0,x0**2)

                    x=symbols('x')
                    f=a1*x**2-c1

                    x3=sqrt(c1/a1)

                    s1 = integrate(f, (x, x3, x0))

                    s=pi*c1**2+s1*4

                    Ss=d*r
                    Sc=Ss-s

                    t=t1*s+t2*Sc
                    tkq=t/1000
                h1=t/1000  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Người ta lát gạch trang trí một mảnh sân hình chữ nhật kích thước $%s$ m $\\times$ $%s$ m như hình vẽ bên dưới, trong đó $(P_1), (P_2)$ là hai parabol đối xứng trục với nhau qua trục đối xứng vuông góc với chiều dài của mảnh sân, $(C)$ là đường tròn có tâm trùng với tâm của mảnh sân và lần lượt có duy nhất một điểm chung với các parabol tại chính các đỉnh của parabol đó (tham khảo hình vẽ)zz Chi phí cho phần lát gạch là $%s$ nghìn đồng một mét vuông, phần không lát gạch để trồng cỏ với chi phí $%s$ nghìn đồng một mét vuôngzz Trong trường hợp hình tròn $(C)$ có diện tích lớn nhất hãy tính tổng chi phí (đơn vị: triệu đồng) lát gạch và trồng cỏ cho mảnh sânzz (kết quả làm tròn tới hàng đơn vị)zz}
                                {\\scalebox{0zz8}{
            \\begin{tikzpicture}[rotate=90]
                \\draw[thick] (-2,-3zz5) -- (-2,3zz5);
                \\draw[thick] (-2,-3zz5) -- (2,-3zz5);
                \\draw[thick] (2,-3zz5) -- (2,3zz5);
                \\draw[thick] (2,3zz5) -- (-2,3zz5);
                \\draw[samples=200,domain=-2:2,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-0zz5});
                \\draw[samples=200,domain=-2:2,smooth,variable=\\x] plot (\\x,{-1*(\\x)^2+0*(\\x)+0zz5});
                \\draw[samples=200,domain=0:360,smooth,variable=\\t]
                plot ({0zz5*cos(\\t)},{0zz5*sin(\\t)});
                \\begin{scope}
                    \\clip (-2,-3zz5) rectangle (2,3zz5);
                    \\fill[red!30, opacity=0zz7] 
                    plot[samples=200,domain=-2:-0zz7,smooth,variable=\\x] 
                    (\\x,{1*(\\x)^2+0*(\\x)+-0zz5})
                    -- plot[samples=200,domain=-0zz7:-2,smooth,variable=\\x] 
                    (\\x,{-1*(\\x)^2+0*(\\x)+0zz5})
                    -- cycle;

                    \\fill[red!30, opacity=0zz7] 
                    plot[samples=200,domain=0zz7:9,smooth,variable=\\x] 
                    (\\x,{1*(\\x)^2+0*(\\x)+-0zz5})
                    -- plot[samples=200,domain=9:0zz7,smooth,variable=\\x] 
                    (\\x,{-1*(\\x)^2+0*(\\x)+0zz5})
                    -- cycle;
                \\end{scope}
                \\fill[red!30, opacity=0zz7] (0,0) circle (0zz5);
            \\end{tikzpicture} }}'''
                                %(latex(d),latex(r),latex(t1),latex(t2)
                                ))

                # Nội dung lời giải
                loigiai = ('''Gắn hệ trục tọa độ $(Oxy)$ như hình vẽ
                        \\begin{center}
                \\scalebox{0zz8}{
                    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                        \\draw[->] (-3,0) -- (3,0) node[below] {$x$};
                        \\draw[->] (0,-4) -- (0,4) node[left] {$y$};
                        \\draw[thick] (-2,-3zz5) -- (-2,3zz5);
                        \\draw[thick] (-2,-3zz5) -- (2,-3zz5);
                        \\draw[thick] (2,-3zz5) -- (2,3zz5);
                        \\draw[thick] (2,3zz5) -- (-2,3zz5);
                        \\draw[samples=200,domain=-2:2,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-0zz5});
                        \\draw[samples=200,domain=-2:2,smooth,variable=\\x] plot (\\x,{-1*(\\x)^2+0*(\\x)+0zz5});
                        \\draw[samples=200,domain=0:360,smooth,variable=\\t]
                        plot ({0zz5*cos(\\t)},{0zz5*sin(\\t)});
                        \\begin{scope}
                            \\clip (-2,-3zz5) rectangle (2,3zz5);
                            \\fill[red!30, opacity=0zz7] 
                            plot[samples=200,domain=-2:-0zz7,smooth,variable=\\x] 
                            (\\x,{1*(\\x)^2+0*(\\x)+-0zz5})
                            -- plot[samples=200,domain=-0zz7:-2,smooth,variable=\\x] 
                            (\\x,{-1*(\\x)^2+0*(\\x)+0zz5})
                            -- cycle;

                            \\fill[red!30, opacity=0zz7] 
                            plot[samples=200,domain=0zz7:9,smooth,variable=\\x] 
                            (\\x,{1*(\\x)^2+0*(\\x)+-0zz5})
                            -- plot[samples=200,domain=9:0zz7,smooth,variable=\\x] 
                            (\\x,{-1*(\\x)^2+0*(\\x)+0zz5})
                            -- cycle;
                        \\end{scope}
                        \\fill[red!30, opacity=0zz7] (0,0) circle (0zz5);
                        \\node at (-0zz2,0zz1) [below] {$O$};
                \\end{tikzpicture} }
                \\scalebox{0zz8}{
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\draw[->] (-3,0) -- (3,0) node[below] {$x$};
                    \\draw[->] (0,-1) -- (0,4) node[left] {$y$};
                    \\draw[thick] (2,3zz5) -- (-2,3zz5);
                    \\draw[thick] (2,0) -- (2,3zz5);
                    \\draw[samples=200,domain=-2:2,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+0*(\\x)+-0zz5});
                    \\draw[samples=200,domain=0:360,smooth,variable=\\t]
                    plot ({0zz5*cos(\\t)},{0zz5*sin(\\t)});
                    \\begin{scope}
                        \\clip (-2,-3zz5) rectangle (2,3zz5);

                        \\fill[red!30, opacity=0zz7] 
                        plot[samples=200,domain=0zz7:9,smooth,variable=\\x] 
                        (\\x,{1*(\\x)^2+0*(\\x)+-0zz5})
                        -- plot[samples=200,domain=9:0zz7,smooth,variable=\\x] 
                        (\\x,{-0*(\\x)^2+0*(\\x)+0})
                        -- cycle;
                    \\end{scope}
                    \\fill[red!30, opacity=0zz7] (0,0) circle (0zz5);
                    \\node at (1zz7,1zz2) {$S_1$};
                    \\node at (-1zz2,2) {$(P)$};
                    \\node at (-0zz2,0zz1) [below] {$O$};
            \\end{tikzpicture} }
            \\end{center}
            Gọi phương trình của parabol quay lên là $(P): y=ax^2-c$ với $a, c > 0$zz \\\\
            $(P)$ đi qua điểm $(%s;%s)$ suy ra $%s a-c=%s \\Leftrightarrow a=\\frac{c+%s}{%s}$zz \\\\
            Gọi phương trình của đường tròn $(C)$ là $x^2+y^2=c^2$ với tâm $O(0;0)$, bán kính $R=c$zz\\\\
            Theo đề bài $(C)$ và $(P)$ có duy nhất một điểm chung tại $(0;-c)$, tức là \\\\
            Hệ phương trình $\\heva{& y=ax^2-c \\\\& x^2+y^2=c^2}$ có nghiệm duy nhấtzz \\\\
            Thế hai phương trình ta được \\\\
            $x^2+(ax^2-c)^2=c^2 (*) \\Leftrightarrow x^2+a^2 x^4-2acx^2=0 \\Leftrightarrow x^2 (a^2 x^2-2ac+1)=0 \\Leftrightarrow \\hoac{& x=0 \\\\& x^2=\\frac{2ac-1}{a^2}}$zz \\\\
            Phương trình $(*)$ có nghiệm duy nhất $x=0$ khi \\\\
            $\\frac{2ac-1}{a^2} \\le 0 \\Leftrightarrow 2ac-1 \\le 0 \\Leftrightarrow 2 \\cdot \\frac{c+%s}{%s} \\cdot c-1 \\le 0 \\Leftrightarrow %s \\le c \\le %s$zz \\\\
            Suy ra bán kính đường tròn lớn nhất là $c_{max}=%s$, khi đó $a=\\frac{c+%s}{%s}=%s$zz \\\\
            Suy ra $(P): y=%s$, $(P)$ cắt $Ox$ tại điểm có hoành độ là nghiệm phương trình \\\\
            $%s=0 \\Leftrightarrow x=\\pm %s$zz \\\\
            Diện tích hình phẳng giới hạn bởi $(P)$ và trục $Ox$  và hai đường $x=%s, x=%s$ là \\\\
            $S_1=\\int \\limits_{%s}^{%s} \\left( %s \\right) \\text{d}x=%s$zz \\\\
            Diện tích hình tròn là $S_t=\\pi R^2=%s \\pi$ m$^2$zz \\\\
            Diện tích phần lát gạch là $S=S_t+4S_1=%s$ m$^2$zz \\\\
            Diện tích mảnh sân là $S_s=%s \\cdot %s =%s$ m$^2$zz \\\\
            Diện tích phần trồng cỏ là $S'=S_s-S=%s-%s=%s$ m$^2$zz \\\\
            Vậy chi phí để lát gạch và trồng cỏ cho mảnh sân là \\\\
            $T=%s S+%s S'=%s \\approx %s$ triệu đồngzz'''
                        %(latex(x0),latex(y0),latex(x0**2),latex(y0),latex(y0),latex(x0**2),
                            latex(y0),latex(x0**2),latex(x1),latex(x2),
                            latex(x2),latex(y0),latex(x0**2),latex(a1),
                            latex(f),latex(f),latex(x3), latex(x3),latex(x0),
                            latex(x3),latex(x0),latex(f),latex(s1),
                            latex(c1**2),
                            latex(s),
                            latex(d),latex(r),latex(Ss),
                            latex(Ss),latex(s),latex(Sc),
                            latex(t1),latex(t2),latex(t),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.')
            return content

